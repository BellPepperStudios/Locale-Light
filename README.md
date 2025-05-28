# Locale Light

Locale Light is a simple, terminal-based chat interface for running local AI models using [Ollama](https://ollama.com/).  
Easily chat with any model you have installed, right from your command line!

---

## ✨ Features

- **Chat with any Ollama model**: Just type `start <model_name>` and begin your conversation.
- **Conversation memory**: The AI remembers your chat history during each session.
- **Easy to use**: Clean, readable interface with helpful commands.
- **Quick setup**: Minimal dependencies, ready to run in seconds.

---

## 🚀 Getting Started

### 1. Install [Ollama](https://ollama.com/) and your favorite models

```sh
ollama list
ollama pull llama3
```

### 2. Clone this repository

```sh
git clone https://github.com/yourusername/locale-light.git
cd locale-light
```

### 3. Install Python requirements

```sh
pip install -r requirements.txt
```

### 4. Run Locale Light

```sh
python main.py
```

---

## 🕹️ Usage

- `start <model_name>` — Start chatting with a model (e.g., `start llama3`)
- `help` — Show available commands
- `install help` — Show Ollama installation help
- `exit` — Exit the chat or application

---

## 📦 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) running locally
- At least one Ollama model installed

---

## 📸 Screenshot

```
========================================
             Locale Light
========================================
Type 'help' for a list of commands.

> start llama3
Chatting with model: llama3
(Type 'exit' to leave chat)

You: Hello!
llama3: Hi there! How can I help you today?
```

---

## 📝 License

MIT License

---
