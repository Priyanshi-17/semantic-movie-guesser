<h2 align="center">🎬 Semantic-Movie-Gusser 🎯</h2>
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

## 🛠️ How It Works

- Movie plots are loaded from JSON files.
- Storylines are embedded using the `all-MiniLM-L6-v2` model.
- Embeddings are stored in FAISS indexes by industry.
- User selects a category (Bollywood+Tollywood or Hollywood).
- A random plot is shown with 4 movie title options.
- User guesses the movies.

---

## 📁 Project Structure

```MovieGame/
├── app/
│ ├── app.py                        # Streamlit frontend
│ └── background1.jpg               # UI background image
├── data/
│ ├── bollywood_tollywood.json      # Bollywood+Tollywood raw movie data
│ └── hollywood.json                # Hollywood raw movie data
├── scripts/
│ ├── embeddings/
│ │ ├── bollywood_tollywood_index/           # FAISS index for Bollywood+Tollywood
│ │ └── hollywood_index/                     # FAISS index for Hollywood
│ ├── ingest_data.py                         # Script to load and convert data to FAISS
│ ├── retriever.py                           # Functions to retrieve relevant movie
│ └── test_faiss.py                          # Script to test FAISS search
├── styles/
│ └── style.css                              # Custom CSS for Streamlit app
├── test.py 
```

## 📸 Website Snapshots

<img width="1855" height="917" alt="image" src="https://github.com/user-attachments/assets/d6f1c74c-a56c-450c-839b-b60bdffa57b5" />

<img width="1840" height="915" alt="image" src="https://github.com/user-attachments/assets/8b0bb16a-8026-4587-ae4a-8ed4526155bd" />


