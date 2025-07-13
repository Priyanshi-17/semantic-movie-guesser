import os
import random
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings

# Base directory of the current file (i.e., 'scripts')
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Full absolute paths to FAISS indexes
index_paths = {
    "Bollywood+Tollywood": os.path.join(CURRENT_DIR, "embeddings", "bollywood_tollywood_index"),
    "Hollywood": os.path.join(CURRENT_DIR, "embeddings", "hollywood_index")
}

def load_vectorstore(index_path):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def get_all_quiz_questions(category: str):
    if category not in index_paths:
        raise ValueError("Invalid category!")

    vectorstore = load_vectorstore(index_paths[category])
    docs = list(vectorstore.docstore._dict.values())
    questions = []

    for doc in docs:
        title = doc.metadata.get("title")
        story = doc.page_content
        if not title or not story:
            continue

        other_titles = [
            d.metadata.get("title") for d in docs
            if d.metadata.get("title") and d.metadata.get("title") != title
        ]

        if len(other_titles) < 3:
            continue

        distractors = random.sample(other_titles, 3)
        options = distractors + [title]
        random.shuffle(options)

        questions.append({
            "storyline": story,
            "options": options,
            "answer": title
        })

    return questions