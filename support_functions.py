# Configuration for the arXiv MCP server requiring the 'stdio' transport
server_config = {
    "arxiv": {
        "command": "arxiv-mcp-server",
        "args": [],
        "transport": "stdio" 
    }
}

def make_string_tool(original_tool):
    async def wrapper(**kwargs):
        # Execute the original tool with the arguments provided by the agent
        result = await original_tool.ainvoke(kwargs)
        
        # If the MCP tool returns a list of blocks, extract the text and join it
        if isinstance(result, list):
            text_parts = []
            for item in result:
                if isinstance(item, dict) and "text" in item:
                    text_parts.append(item["text"])
                else:
                    text_parts.append(str(item))
            return "\n".join(text_parts)
            
        # Guarantee a string return for anything else
        return str(result)
        
    return wrapper