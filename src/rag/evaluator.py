from openai import OpenAI
from config.settings import llm_model, open_ai_api_key

client = OpenAI(api_key=open_ai_api_key)


def retrieval_precision(retrieved_docs, user_query):
    """
    Calculates precision of retrieved documents against the user query.
    Precision = (Number of Relevant Docs) / (Total Retrieved Docs)
    Returns a float between 0.0 and 1.0.
    """
    if not retrieved_docs:
        return 0.0

    relevant_count = 0
    total_docs = len(retrieved_docs)

    for doc in retrieved_docs:
        prompt = (
            f"Given the user query: '{user_query}'\n"
            f"And the retrieved document: '{doc}'\n\n"
            f"Is this document directly relevant to answering the user's query? "
            f"Answer ONLY with 'YES' or 'NO'."
        )
        try:
            response = client.chat.completions.create(
                model=llm_model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            answer = response.choices[0].message.content.strip().upper()
            if "YES" in answer:
                relevant_count += 1
        except Exception as e:
            print(f"[Eval Warning] Precision check failed for a doc: {str(e)}")

    return relevant_count / total_docs


def answer_relevance(answer, user_query):
    """
    Scores the final answer's relevance to the user query on a scale of 0 to 5.
    Returns a tuple: (score [float], reason [str])
    """
    if not answer or "I am sorry" in answer:
        return 0.0, "Answer was empty or a fallback response."

    prompt = (
        f"User Query: '{user_query}'\n"
        f"System Answer: '{answer}'\n\n"
        f"Evaluate the exact relevance of the System Answer to the User Query on a scale of 0 to 5, "
        f"where 5 is a perfect, direct, and complete answer. \n"
        f"Return your evaluation STRICTLY in the following format:\n"
        f"Score: <number>\nReason: <one sentence explanation>"
    )

    try:
        response = client.chat.completions.create(
            model=llm_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = response.choices[0].message.content.strip()

        # Simple parsing
        score_line = [
            line for line in content.split("\\n") if line.startswith("Score:")
        ]
        reason_line = [
            line for line in content.split("\\n") if line.startswith("Reason:")
        ]

        score = 0.0
        reason = "Parsing failed"

        if score_line:
            try:
                score = float(score_line[0].replace("Score:", "").strip())
            except Exception as e:
                print(e)
        if reason_line:
            reason = reason_line[0].replace("Reason:", "").strip()

        return score, reason
    except Exception as e:
        return 0.0, f"Evaluation API call failed: {str(e)}"
