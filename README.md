# Fetch, Aggregate, Chat

A simple agentic RAG system that searches the web, scrapes relevant pages, chunks the content intelligently, and lets you ask questions about any topic using an LLM.

---

## Workflow

1. You enter a topic.
2. A search agent queries the web and returns the top relevant URLs.
3. A scraping agent visits and extracts the content from those URLs.
4. A chunking agent processes and splits the content into self-contained, context-rich chunks.
5. The chunks are embedded and stored in a FAISS vector index.
6. You ask questions. Your query is embedded, the most relevant chunks are retrieved, and an LLM answers using only that context.

---

## Screenshots

Screenshots of the app in action are attached separately.

---

## Repo Structure

```
FAC/
├── app.py                           # Entry point
├── requirements.txt                 # Dependencies
├── config/
│   └── settings.py                  # All config (model names, keys, paths, top-k values)
├── src/
│   ├── agents/
│   │   ├── crew_agent.py           # Assembles the CrewAI crew
│   │   └── sub_agents/
│   │       ├── search_agent.py
│   │       ├── scraping_agent.py
│   │       └── chunking_agent.py
│   ├── tasks/
│   │   ├── searching_task.py
│   │   ├── scraping_task.py
│   │   └── chunker_task.py
│   ├── tools/
│   │   ├── search_tool.py          # DuckDuckGo search wrapper
│   │   └── scraper_tool.py         # HTTP scraper
│   └── rag/
│       ├── embedder.py             # Embeds chunks via sentence-transformers
│       ├── indexer.py              # Builds FAISS index
│       ├── retriever.py            # Retrieves top-k chunks for a query
│       └── llm.py                  # Calls OpenAI and formats the answer
└── task_data/                      # Intermediate agent outputs saved here
```

---

## How to Run Locally

1. Set your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_key_here
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```
   (use `python3` if needed)

4. Enter a topic when prompted and wait for the agents to search and scrape.

5. Once ready, ask any questions about the topic. Type `bye`, `quit`, or `exit` to stop.

---

## Author

**Sagnik Mukherjee**  
[GitHub Profile](https://github.com/sagnik0712mukherjee)