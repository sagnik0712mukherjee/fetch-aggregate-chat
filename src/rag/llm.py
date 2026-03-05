from src.rag.retriever import retrieve_results
from openai import OpenAI
from config.settings import open_ai_api_key, llm_model, rag_top_k

client = OpenAI(api_key=open_ai_api_key)


def llm_response(user_query, docs, index):

    context_docs = retrieve_results(user_query, docs, index, rag_top_k)

    print(f"\n\ncontext_docs\n{context_docs}\n\n\n")
    context = "\n".join(f"- {doc}" for doc in context_docs)

    prompt = (
        f"Use ONLY the context below to answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {user_query}\n"
        f"Answer:"
        f"If context does not provide information about the sought query, just return 'I am sorry, I am unable to answer your question due to lack of knowledge!'"
    )

    try:
        response = client.chat.completions.create(
            model=llm_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[LLM Error] I encountered an error while processing your request: {str(e)}"
