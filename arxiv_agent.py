import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from support_functions import server_config, make_string_tool
from dotenv import load_dotenv
from system_prompt import SYSTEM_PROMT

load_dotenv()

print("[LOG] Imported libraries")

async def main():

    # 1. Initialize the client directly
    client = MultiServerMCPClient(server_config)

    # 2. Fetch the tools from the arXiv server asynchronously
    mcp_tools = await client.get_tools()

    stringified_tools = []
    for t in mcp_tools:
        stringified_tools.append(
            StructuredTool.from_function(
                coroutine=make_string_tool(t),
                name=t.name,
                description=t.description,
                args_schema=t.args_schema
            )
        )

    # 3. Initialize your model
    my_api_key = os.getenv("SARVAM_API_KEY")
    model = ChatOpenAI(model="sarvam-105b",
                       api_key=my_api_key, 
                       base_url="https://api.sarvam.ai/v1",
                       max_tokens=2048,
                       temperature=0.1)

    # 4. Create the ReAct agent
    agent = create_react_agent(model, tools=stringified_tools)

    # 5. Define the query
    while True:
        print("------------------------------------------------------")
        query = input(f"\n\nWhat do you want to search: ")
        if query == "quit": break
    
        print("🚀 Agent started. Tracking thought process...\n")
        print("-" * 50)
        
        # --- New Streaming Execution ---
        final_output = ""
        chat_history = [{'role':'system', "content": SYSTEM_PROMT},
                        {"role": "user", "content": query}]
        
        # stream_mode="updates" yields data every time a node finishes
        async for step in agent.astream({"messages": chat_history}, stream_mode="updates"):
            for node, values in step.items():
                
                if node == "agent":
                    message = values["messages"][-1]
                    if message.tool_calls:
                        for tool_call in message.tool_calls:
                            print(f"🛠️  Agent is calling tool: {tool_call['name']}")
                            print(f"   Arguments: {tool_call['args']}\n")
                    else:
                        final_output = message.content
                        
                elif node == "tools":
                    message = values["messages"][-1]
                    print(f"✅  Tool '{message.name}' completed.")
                    # Slice the first 150 characters of the result to keep the terminal clean
                    snippet = str(message.content)[:150].replace('\n', ' ')
                    print(f"   Result snippet: {snippet}...\n")
    
        print("=" * 50)
        print("FINAL OUTPUT:\n")
        print(final_output)

if __name__ == "__main__":
    asyncio.run(main())