from crewai import Task
from src.agents.sub_agents.chunking_agent import chunk_based_on_obtained_data
from config.settings import task_data_path


def get_chunking_task():

    chunking_agent = chunk_based_on_obtained_data()

    chunking_task = Task(
        description="""
            Process the raw text obtained from the web search and web scraper agents and produce
            contextually rich, self-contained chunks for a RAG vector database.

            Rules:
            - Every chunk must stand alone — a reader with no other context must understand what it describes.
            - Every chunk must explicitly name the product/subject (e.g. "iPhone 14 Pro" not just "the Pro model").
            - Tables: convert each row into a full sentence that includes the row header, column header, and value
              (e.g. "iPhone 14 was launched on September 16, 2022 in the United States.").
            - Images: describe what the image shows as a plain-text sentence.
            - Group related short bullets about the same subject into one multi-sentence chunk.
            - Strip all HTML tags, markdown syntax (##, **, ---, etc.), and raw URLs.
            - Do NOT produce chunks that are bare headings, separator lines, or single words.
        """,
        expected_output="""
            A single flat JSON array of strings. Each string is a self-contained, meaningful chunk of
            information. No markdown code fences, no ```json, no extra keys — only the raw array.
        """,
        agent=chunking_agent,
        markdown=True,
        output_file=f"{task_data_path}/chunking.md",
    )

    return chunking_task
