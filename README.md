# 🧠 Ollama CLI Chat Assistant

A cross-platform, Python-based **CLI tool** to interact with local LLMs (like LLaMA3) using [Ollama](https://ollama.com/). Get AI responses in your terminal — with real-time streaming output and no API key required!

---

## 🎯 Features

- ✅ Chat with local LLMs from the terminal
- ⚡ Real-time **streaming output**
- 🔄 Typing-like effect with a spinner while the model is thinking
- 🖥️ Works on **macOS, Windows, and Linux**
- 🔓 No OpenAI key or paid API — uses Ollama locally

---

## 🧱 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running (default port: `11434`)
- A supported model like `llama3` pulled via Ollama

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ollama-cli-chat.git
cd ollama-cli-chat
```

### 2. (Optional) Create a virtual environment

```bash
pip install -r requirements.txt
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the model using Ollama

```bash
ollama pull llama3
```

### 5. Run the chat tool

```bash
python main.py
```

## 📸 Demo

```bash
💬 You: What's the capital of France?
🤖 AI is thinking... |
🧠 AI: The capital of France is Paris.
```

## 📂 File Structure

```bash
ollama-cli-chat/
├── main.py              # Entry point
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🧠 How It Works

-	Uses requests to call Ollama’s generate endpoint
-	Handles real-time streaming token output
-	Displays a spinner while waiting for a response

## 🛠️ Future Improvements

-	Support for chat history
-	Model switching during runtime
- Optional markdown rendering

## 🤝 Contributing

Contributions are welcome!
Feel free to fork, suggest improvements, or raise issues.

## 📄 License

MIT License © 2025 [Arun Sai Veerisetty]
