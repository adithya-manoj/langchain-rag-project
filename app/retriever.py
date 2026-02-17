from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

INDEX_PATH = "faiss_index"


def load_retriever():
    # IMPORTANT: Use same embedding model as ingestion
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return retriever


if __name__ == "__main__":
    retriever = load_retriever()

    query = input("Enter your question: ")
    docs = retriever.invoke(query)

    print("\nRetrieved Documents:\n")
    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc.page_content)
        print()
