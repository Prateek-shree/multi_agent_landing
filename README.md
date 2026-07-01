# 🔬 AgentMatrix – Multi-Agent AI Research System

> An AI-powered research assistant built with **LangChain**, **Mistral AI**, **Tavily Search**, and **Streamlit** that automates the complete research workflow using multiple specialized AI agents.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Agentic-1C3C3C?style=for-the-badge)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

## 🚀 Live Demo

### 🌐 Project Landing Page
**https://multi-agent-system-26.streamlit.app/**

> Explore the project architecture, workflow, technology stack, and output format.

---

# 📌 Overview

AgentMatrix is a **Multi-Agent AI Research System** that divides the research process into multiple intelligent agents.

Instead of asking a single language model to do everything, each agent is responsible for one specialized task:

- Search the web
- Read and extract information
- Generate a professional research report
- Critique and evaluate the final report

This modular architecture produces more structured, reliable, and explainable research than a single-prompt approach.

---

# ✨ Features

- 🔍 Live web research using Tavily Search
- 📄 Intelligent web content extraction
- 🤖 LangChain-powered multi-agent workflow
- ✍️ AI-generated research reports
- 🧐 Automatic report evaluation
- 📚 Markdown report generation
- ⚡ Modular and extensible architecture
- 🎨 Professional Streamlit interface

---

# 🏗️ System Architecture

```text
                   User Query
                        │
                        ▼
             ┌────────────────────┐
             │  Search Agent      │
             │  (Tavily Search)   │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │  Reader Agent      │
             │  Web Scraping      │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │  Writer Agent      │
             │  Report Generator  │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │  Critic Agent      │
             │  Report Reviewer   │
             └─────────┬──────────┘
                       │
                       ▼
           Professional Research Report
```

---

# 🧠 Multi-Agent Workflow

### 🔍 Search Agent

- Searches the web for recent information
- Collects trusted URLs
- Retrieves summaries and snippets

---

### 📄 Reader Agent

- Opens the most relevant webpage
- Extracts clean textual content
- Removes unnecessary HTML elements

---

### ✍️ Writer Agent

Generates a structured report containing:

- Introduction
- Key Findings
- Conclusion
- Sources

---

### 🧐 Critic Agent

Evaluates the generated report by providing:

- Overall Score
- Strengths
- Weaknesses
- Suggestions
- Final Verdict

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| AI Framework | LangChain |
| LLM | Mistral AI |
| Search API | Tavily |
| Web Scraping | BeautifulSoup |
| UI | Streamlit |
| Environment | Python-dotenv |

---

# 📂 Project Structure

```text
AgentMatrix/

├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Prateek-shree/multi_agent_system.git
```

Move into the project

```bash
cd multi_agent_system
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 📊 Output

The application automatically generates:

- Detailed research report
- Sources used
- Quality evaluation
- Research score
- Suggestions for improvement

---

# 🎯 Future Improvements

- PDF Export
- Citation Formatting
- Multi-source Verification
- Report History
- Agent Memory
- RAG Integration
- LangGraph Visualization
- Authentication
- Multi-language Research
- Streaming Responses

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

