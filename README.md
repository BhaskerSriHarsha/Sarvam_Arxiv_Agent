# Sarvam_Arxiv_Agent
<img src="banner.png"></img>
A ReAct agent powered by Sarvam models to perform agentic survey of Arxiv papers

---

### Prerequisites
Before you begin, ensure you have the following installed:
* **Python 3.11** or higher
* **Git**
* A valid **Sarvam API Key**

### 1. Clone the Repository
Open your terminal and clone this repository to your local machine:
```bash
git clone https://github.com/BhaskerSriHarsha/Sarvam_Arxiv_Agent.git
cd Sarvam_Arxiv_Agent
```

### 2. Install the arXiv MCP Server
This agent relies on the arXiv Model Context Protocol (MCP) server. It must be installed globally on your system so the LangGraph agent can spawn it as a background process.

Using `uv` (Recommended):
```bash
pip install uv
uv tool install git+https://github.com/blazickjp/arxiv-mcp-server
uv tool update-shell
```
*(Note: If you use `uv tool update-shell` on Windows, you will need to close and reopen your terminal for the changes to take effect).*

### 3. Set Up the Virtual Environment
Create an isolated Python environment and install the required dependencies using the provided `requirements.txt` file.

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Environment Variables
The agent requires your Sarvam API key to function. We use a `.env` file to keep this secure locally.

1. Create a new file named exactly `.env` in the root directory of the project.
2. Add your API key to the file like this (no spaces around the equals sign, no quotes):
```text
SARVAM_API_KEY=your_actual_api_key_here
```
*Security Note: Ensure your `.gitignore` file includes `.env` so you do not accidentally commit your API key.*

### 5. Run the Agent
With your environment activated and your API key set, you are ready to run the literature survey agent:

```bash
python arxiv_agent.py
```

### 6. View Your Report
You will see the agent's thought process stream in the terminal. Once the execution is complete, the agent will synthesize its findings and save them locally. Open the newly generated `report.md` file in your preferred Markdown viewer to read the final academic survey.

# To Do
1. <s> Add a good system prompt </s>
2. Add web_search tool
3. <s> Create requirements.txt </s>
4. <s> Add a report_writing tool </s>
5. <s> Add instructions to run the script in README file </s>
6. Add conversational memory to the agent