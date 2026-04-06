from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

def osint_scan(target_ip):
    return f'Scanning {target_ip} for open ports and CVEs...'

# Initialize local LLM
# llm = Ollama(model='llama3')

print('ThreatGPT Agent initializing... 🚧')
