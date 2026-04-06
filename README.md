# ThreatGPT: Autonomous OSINT Research Agent 🤖🔎

> **STATUS: IN PROGRESS 🚧**
> The LangChain scaffolding and custom Python lookup tools (`NVD`, `Shodan`) are completed and packaged. The project is specifically paused while awaiting the installation/binding of a local powerful Large Language Model (like Llama-3 running on Ollama) to serve as the agent's brain.

---

## 📖 The "Analyst Fatigue" Problem
Modern Cyber Threat Intelligence (CTI) requires Blue Team analysts and security integrators to manually pivot between dozens of tabs: querying Shodan for exposed ports, cross-referencing NIST vulnerability databases (NVD) for CVE severity, parsing hacker forums, and writing endless debrief reports. It is incredibly tedious and heavily prone to human exhaustion.

## 🚀 The ThreatGPT Solution
**ThreatGPT** attempts to completely automate OSINT research workflows. It is a completely autonomous Python-based intelligence agent. By leveraging the revolutionary `LangChain` framework alongside local Large Language Models (LLMs), ThreatGPT acts as an artificial junior security analyst. You assign it a target IP address or a malware hash, and the model literally "thinks" about which tools to use, executes API calls autonomously to gather data, and synthesizes everything into a professional, human-readable Intelligence Briefing.

## 🧠 Architecture & Capabilities
1. **The Core Brain**: Operates purely on Local LLMs (such as Llama-3 operated through `Ollama`). This ensures zero data leaks—highly critical for OPSEC.
2. **LangChain Tool Integration**: Custom Python functions (like `shodan_host_scan` or `nvd_cve_lookup`) are tightly wrapped in LangChain `Tool` classes. The LLM can dynamically trigger these Python functions whenever it encounters unstructured OSINT tasks.
3. **Zero-Shot ReAct Loop**: The AI follows a continuous *Observation -> Thought -> Action* decision loop until the intelligence target has been fully investigated.
4. **Vector Memory (RAG)**: Integration of `ChromaDB` allows the agent to recall past intelligence reports from the organization internally without hallucinating.

## 💻 Technical Stack
* **AI Orchestration Framework**: LangChain
* **LLM Provider**: Ollama (Running local Llama-3)
* **Embedding/Vector Database**: ChromaDB
* **Tool Interfaces**: Requests (Standard Python Web Wrapper)

## 🛣️ Current Roadmap
- [x] Architect repository infrastructure
- [x] Wrap OSINT scanners perfectly inside custom LangChain `Tools`
- [x] Define execution environment logic and script handling
- [ ] Inject raw API Keys (Shodan/NVD) into an invisible `.env` file
- [ ] Initialize local binding to Ollama inference engine
- [ ] Run full system end-to-end integration test against a predefined target server 
