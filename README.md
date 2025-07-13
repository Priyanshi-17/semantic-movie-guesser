# semantic-movie-guesser

# 🎬 AI Movie Guessing Game

An interactive AI-powered guessing game where users try to guess the movie based on storyline snippets. The system uses semantic search to retrieve relevant movie storylines from a local vector database built with FAISS and HuggingFace embeddings.

---

## 🚀 Features

- 🔍 Semantic search over Bollywood, Tollywood, and Hollywood movie plots
- 🤖 Vector search using FAISS and HuggingFace embeddings (`all-MiniLM-L6-v2`)
- 🧠 LangChain integration for document and vector handling
- 🎮 Streamlit-based interactive UI
- 🎯 Guess feedback system based on string similarity
- 🧵 Separate FAISS index for different movie industries

---

## 🛠️ Tech Stack

| Category       | Tools/Libs Used                                 |
|----------------|-------------------------------------------------|
| Embeddings     | `HuggingFace Embeddings` (MiniLM-L6-v2)         |
| Vector Store   | `FAISS`                                         |
| Framework      | `LangChain`, `Streamlit`                        |
| Language       | `Python`                                        |
| Data Handling  | `JSON`, `os`               |

---

## 📁 Project Structure

<pre> <code> ## 📁 Project Structure ``` ├── app │ └── app.py # Streamlit frontend ├── embeddings │ ├── hollywood_index/ # FAISS index for Hollywood │ └── bollywood_tollywood_index/ # FAISS index for Bollywood+Tollywood ├── data │ ├── bollywood_tollywood.json # Raw movie data │ └── hollywood.json ├── utils │ ├── build_faiss.py # Embedding + FAISS creation script │ └── helpers.py # Utility functions for guessing logic ├── README.md └── requirements.txt ``` </code> </pre>


