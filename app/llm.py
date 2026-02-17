"""
LLM Configuration and Initialization

Handles initialization and configuration of the Language Model
used for generating responses in the RAG pipeline.
"""

import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()


def get_llm(
    temperature: float = 0.0,
    model: Optional[str] = None,
    max_tokens: int = 1024,
) -> BaseChatModel:
    """
    Initialize and return a configured ChatOpenAI model.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    model_name = model or os.getenv("OPENAI_MODEL", "gpt-4o")

    try:
        llm = ChatOpenAI(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=60,
            max_retries=2,
        )
        return llm

    except Exception as e:
        raise RuntimeError(f"Failed to initialize LLM: {str(e)}")
