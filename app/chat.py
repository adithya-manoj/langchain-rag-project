from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from app.retriever import load_retriever


def main():
    retriever = load_retriever()

    llm = ChatOllama(model="mistral")

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant answering questions based ONLY on the provided context.

If the answer is not in the context, say "I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
""")

    print("RAG Chat System Ready")

    while True:
        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        chain = prompt | llm

        response = chain.invoke({
            "context": context,
            "question": question
        })

        print("\nAnswer:\n")
        print(response.content)


if __name__ == "__main__":
    main()
