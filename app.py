from src.agents.crew_agent import build_crew
from config.settings import web_top_k, exit_queries
import json

from src.rag.indexer import index_faiss_docs
from src.rag.llm import llm_response
from src.rag.guardrails import validate_chunks, validate_query
from src.rag.evaluator import retrieval_precision, answer_relevance
from src.rag.retriever import retrieve_results
from config.settings import eval_top_k_precision, rag_top_k

user_topic = input("Which topic would you like to explore today?\n")

try:
    crew_super_agent = build_crew(user_topic, web_top_k)
    crew_result_str = str(crew_super_agent.kickoff())
    crew_result = json.loads(crew_result_str)

    # Apply Guardrail 1: Validate Document Chunks
    valid_chunks = validate_chunks(crew_result)

    index = index_faiss_docs(valid_chunks)
except Exception as e:
    print(f"\n[Fatal Error] Application initialization failed: {str(e)}")
    exit(1)

print("Now, you may ask Questions based on your topic...")
print("(Type 'bye' / 'quit' / 'exit' to quit the app...)")

if __name__ == "__main__":
    while True:
        user_query = input("Your Question\n")
        if not user_query:
            continue

        if user_query.lower() not in exit_queries:
            try:
                # Apply Guardrail 2: Validate User Query
                clean_query = validate_query(user_query)

                response = llm_response(clean_query, valid_chunks, index)
                print(f"\nBot: {response}\n")

                # --- Evaluation Metrics ---
                try:
                    # To calculate precision, we need the exact retrieved docs.
                    # llm_response internally fetches them, but we'll fetch them here again just for eval
                    # (In a larger app, llm_response should return them alongside the answer)
                    context_docs = retrieve_results(
                        clean_query, valid_chunks, index, rag_top_k
                    )

                    if eval_top_k_precision:
                        precision = retrieval_precision(context_docs, clean_query)
                        print(f"   [Eval] Retrieval Precision: {precision:.2f}")

                    relevance_score, reason = answer_relevance(response, clean_query)
                    print(
                        f"   [Eval] Answer Relevance: {relevance_score}/5.0 — {reason}\n"
                    )
                except Exception as eval_err:
                    print(
                        f"   [Eval Error] Could not compute metrics: {str(eval_err)}\n"
                    )

            except ValueError as ve:
                print(f"\n[Validation Error] {str(ve)}\n\n")
            except Exception as e:
                print(f"\n[System Error] {str(e)}\n\n")
        else:
            break
