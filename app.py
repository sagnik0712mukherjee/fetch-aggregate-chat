from src.agents.crew_agent import build_crew
from config.settings import web_top_k, exit_queries
import json

from src.rag.indexer import index_faiss_docs
from src.rag.llm import llm_response

user_topic = input("Which topic would you like to explore today?\n")

crew_super_agent = build_crew(user_topic, web_top_k)
crew_result = json.loads(str(crew_super_agent.kickoff()))

index = index_faiss_docs(crew_result)

print("Now, you may ask Questions based on your topic...")
print("(Type 'bye' / 'quit' / 'exit' to quit the app...)")

if __name__ == "__main__":
    while True:
        user_query = input("Your Question\n")
        if not user_query:
            continue

        if user_query.lower() not in exit_queries:
            print(f"\nBot: {llm_response(user_query, crew_result, index)}\n\n")
        else:
            break
