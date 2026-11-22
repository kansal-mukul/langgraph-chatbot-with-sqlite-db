# LangGraph Basics

This repository contains small examples that build on one another to demonstrate LangGraph, chat history, streaming, and checkpoint persistence. The chat examples use [LangChain](https://python.langchain.com/) with a Groq-hosted language model and [Streamlit](https://streamlit.io/) for the interface.

## Requirements

- Python 3.13 or later
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A Groq API key to run the chat examples

## Set up

Open PowerShell in the project directory and install the dependencies:

```powershell
uv sync
```

The chat backends read `GROQ_API_KEY` from the environment. For local development, create a `.env` file in the project directory:

```text
GROQ_API_KEY=your_groq_api_key
```

Keep your API key private. Do not commit `.env` or local chat database files.

## Examples

### Basic LangGraph

Run the standalone graph:

```powershell
uv run main.py
```

It invokes a graph that greets the name supplied in `main.py`.

### Streamlit chat apps

Run one of the frontends from the project directory:

```powershell
# Basic chat interface
uv run streamlit run 3_streamlit_frontend.py

# Stream assistant responses as they are generated
uv run streamlit run streamlit_frontend_streaming.py

# In-memory checkpointing with multiple conversation threads
uv run streamlit run streamlit_frontend_threading.py

# SQLite-backed checkpointing that persists conversations
uv run streamlit run streamlit_frontend_database.py
```

Streamlit opens the selected app in your browser. The database-backed version stores LangGraph checkpoints in `chatbot.db` in the project directory, so conversations can be retrieved after restarting the app. The other chat backends use an in-memory checkpointer, so their checkpointed conversations are lost when the process stops.

#### SQLite-backed chat output

1. Run `uv run streamlit run streamlit_frontend_database.py` from the project directory.
2. Open the local URL printed by Streamlit in your browser (usually `http://localhost:8501`).
3. Enter a message in the chat box and submit it. The user message and the assistant response appear in the conversation.
4. Select **New Chat** to start another thread, or select a conversation in **My Conversations** to load it again.
5. Stop and restart the app. Saved conversations remain available because their LangGraph checkpoints are stored in `chatbot.db`.

Example app output:

![SQLite-backed LangGraph chatbot showing saved conversation threads and chat messages](assets/langgraph-chatbot.png)

### How the chat examples work

- `langgraph_backend.py` defines the chat graph and uses an in-memory checkpointer.
- `langgraph_database_backend.py` defines the chat graph with `SqliteSaver` and provides a helper to retrieve saved conversation thread IDs.
- `3_streamlit_frontend.py` provides the basic Streamlit chat UI.
- `streamlit_frontend_streaming.py` streams assistant output to the UI.
- `streamlit_frontend_threading.py` lets you create and switch between conversation threads while the app is running.
- `streamlit_frontend_database.py` uses the SQLite-backed graph to load and continue saved threads.

All chat examples use the Groq model configured in the backend. The SQLite database is local application data; avoid committing it if it contains conversation content.
