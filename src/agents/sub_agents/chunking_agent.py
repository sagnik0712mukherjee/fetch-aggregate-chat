from crewai import Agent


def chunk_based_on_obtained_data():

    chunking_agent = Agent(
        role="Intelligent Data Chunker",
        goal=(
            "Transform raw scraped web content into an array of self-contained, contextually rich text chunks "
            "suitable for a vector database. Every chunk MUST independently convey its meaning — never output an "
            "isolated heading, bullet fragment, or single word. Follow these rules strictly:\n"
            "1. CONTEXT INJECTION: Every chunk must explicitly name the subject it describes "
            "(e.g. 'iPhone 16 Pro features a 48MP main camera...' — never just '48MP main camera...').\n"
            "2. TABLES: Decompose each table row into a standalone sentence that includes the column header and the subject "
            "(e.g. 'iPhone 14 was released on September 16, 2022.').\n"
            "3. IMAGES: Describe any image in plain text as a chunk "
            "(e.g. 'Image shows a side-by-side comparison of iPhone 13 and iPhone 14 camera modules.').\n"
            "4. GROUPING: Merge short related bullets under the same subject into one multi-sentence chunk.\n"
            "5. CLEAN UP: Strip all HTML tags, markdown symbols, and URLs. Keep only meaningful prose.\n"
            "Output a single flat JSON array of strings. No markdown fences, no extra keys."
        ),
        backstory=(
            "You are an expert at preparing text for vector databases. You know that retrieval quality "
            "depends entirely on each chunk being independently understandable. Orphan fragments like '---' "
            "or bare headings are useless — you always produce rich, subject-aware sentences."
        ),
        verbose=True,
    )

    return chunking_agent
