import os

# ====== LLM Settings ======
llm_model = "gpt-4o-mini"
open_ai_api_key = os.environ.get("OPENAI_API_KEY")

# ====== Embedding Settings ======
embedding_model = "all-MiniLM-L6-v2"

# ====== Paths ======
task_data_path = "task_data"

# ====== Retrieval Settings ======
web_top_k = 5
rag_top_k = 3

# ====== User Chat Exit Queries ======
exit_queries = ["bye","quit","exit"]

