# LangChain RAG Project

A clean, scalable Python application for building Retrieval-Augmented Generation (RAG) systems using LangChain.

## Project Structure

```
langchain-rag-project/
├── app/              # Core application modules
│   ├── llm.py        # LLM configuration and initialization
│   ├── prompts.py    # Prompt templates
│   ├── ingest.py     # Document loading, chunking, embeddings
│   ├── retriever.py  # Vector database retrieval logic
│   ├── chat.py       # Main chat / RAG pipeline
│   └── memory.py     # Conversation memory management
├── data/             # Document storage directory
├── ui/               # User interface components
│   └── cli.py        # Command line interface
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

4. **Add documents:**
   - Place your documents in the `data/` directory (e.g. `.txt` files; see `data/README.md`).

5. **Run the application:**
   - **Ingest documents** (build the FAISS index from `data/`):
     ```bash
     python -m app.ingest
     ```
   - **Chat/CLI** (RAG Q&A) is not implemented yet; once `retriever`, `chat`, and `ui/cli` are wired up, you will run:
     ```bash
     python -m ui.cli
     ```

## Features

- **Modular Architecture**: Separated concerns for easy maintenance and extension
- **Document Ingestion**: Support for multiple document formats
- **Vector Retrieval**: Efficient similarity search for relevant context
- **RAG Pipeline**: Combines retrieval and generation for accurate responses
- **Conversation Memory**: Optional support for multi-turn conversations

## Next Steps

1. Implement LLM initialization in `app/llm.py`
2. Create prompt templates in `app/prompts.py`
3. Build document ingestion pipeline in `app/ingest.py`
4. Set up vector database retrieval in `app/retriever.py`
5. Orchestrate the RAG pipeline in `app/chat.py`
6. Add CLI interface in `ui/cli.py`

## License

MIT


