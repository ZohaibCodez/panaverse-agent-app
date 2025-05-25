# 🚀 Panacloud Agent App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Built with Chainlit](https://img.shields.io/badge/Built%20with-Chainlit-ff69b4)](https://github.com/Chainlit/chainlit)
[![OpenAI Agents SDK](https://img.shields.io/badge/OpenAI-Agents%20SDK-brightgreen)](https://github.com/openai/openagents)

---

An AI agent app powered by OpenAI's Agents SDK and Chainlit, built to demonstrate autonomous workflows and tool integration. This app is capable of performing dynamic tasks and visualizing its behavior graphically, making it a powerful educational and development tool for modern AI engineering.

---

## 🧠 Features

- 🔧 Uses OpenAI Agents SDK to create intelligent, modular agents
- 📊 Generates dynamic visualizations using `draw_graph()`
- 💬 Built with Chainlit for interactive chat-based interfaces
- 🧩 Designed for extendability with tools and modular actions

---

## 🧰 Tech Stack

- Python 3.12
- [Chainlit](https://docs.chainlit.io)
- [OpenAI Agents SDK](https://github.com/openai/openagents)
- Graphviz (for visualization)
- `uv` (for managing virtual environments and dependencies)

---

## 📦 Requirements

### `pyproject.toml`

```toml
[project]
name = "panacloud-agent-challange"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"

dependencies = [
    "chainlit>=2.5.5",
    "openai-agents[viz]>=0.0.16",
]

````

---

## 📁 Project Structure

```
panacloud-agent-app/
├── panacloud_agents/      # Agent logic
├── tools/                 # Custom tools
├── assets/                # Graph visualizations (PNG)
├── main.py                # Main entrypoint
├── LICENSE
├── README.md
└── pyproject.toml
```

---

## ⚙️ Usage

Follow these commands to run the agent and visualize its behavior:

```bash
# 1. Install required tools
uv add openai-agents python-dotenv chainlit

# 2. Create and activate virtual environment
uv venv
source .venv/bin/activate

# 3. Run the project
uv run chainlit run main.py -w
```

---

## 📸 Visualization

Use the built-in visualization tool to generate a graph of your agent:

```python
from agents.extensions.visualization import draw_graph

draw_graph(panacloud_agent, filename="assets/agent_graph")
```

The image `agent_graph.png` will be saved in the `assets/` folder.

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome! Feel free to fork the repo and submit a pull request.

---

## 👤 Author

**Zohaib Khan**
Cloud Native & AI Enthusiast

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

