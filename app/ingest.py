"""
Document ingestion: load → chunk → embed → store in FAISS
"""

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "data"
INDEX_PATH = "faiss_index"


def ingest_documents():
    # 1️⃣ Load documents
    loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader
    )
    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    # 2️⃣ Split documents into chunks
    # Because LLMs have token limits.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    # 3️⃣ Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 4️⃣ Store in FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 5️⃣ Save index locally
    vectorstore.save_local(INDEX_PATH)

    print("Ingestion complete. FAISS index saved.")


if __name__ == "__main__":
    ingest_documents()
