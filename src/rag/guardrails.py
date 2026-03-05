from config.settings import (
    min_chunk_length,
    max_chunk_length,
    min_chunk_count,
    max_query_length,
)


def validate_chunks(chunks):
    """
    Validates rules for chunk array output before indexing.
    Filters out chunks that are too short or too long.
    Raises ValueError if remaining valid chunks are too few.
    """
    if not isinstance(chunks, list):
        raise ValueError(f"Expected chunks to be a list, got {type(chunks)}.")

    valid_chunks = []
    for chunk in chunks:
        if isinstance(chunk, str):
            length = len(chunk.strip())
            if min_chunk_length <= length <= max_chunk_length:
                valid_chunks.append(chunk.strip())
            else:
                print(f"[Guardrail] Dropped chunk of length {length} (out of bounds).")

    if len(valid_chunks) < min_chunk_count:
        raise ValueError(
            f"[Guardrail] Agent output yielded {len(valid_chunks)} valid chunks, minimum required is {min_chunk_count}."
        )

    return valid_chunks


def validate_query(query):
    """
    Validates user query before running RAG.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("[Guardrail] Query cannot be empty.")

    cleaned_query = query.strip()

    if len(cleaned_query) > max_query_length:
        raise ValueError(
            f"[Guardrail] Query length ({len(cleaned_query)}) exceeds maximum allowed ({max_query_length})."
        )

    return cleaned_query
