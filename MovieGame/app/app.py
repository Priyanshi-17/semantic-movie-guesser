import streamlit as st
import os
import sys
import random
import base64

# --- Background Image Setup ---
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("background1.jpg")  

# --- Add parent directory to import retriever ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.retriever import get_all_quiz_questions

# --- CSS Styling ---
css_path = os.path.join(os.path.dirname(__file__), "..", "styles", "style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Session State Initialization ---
if "category" not in st.session_state:
    st.session_state.category = None
if "question" not in st.session_state:
    st.session_state.question = None
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "all_questions" not in st.session_state:
    st.session_state.all_questions = None
if "used_titles" not in st.session_state:
    st.session_state.used_titles = set()

# --- Title ---
if not st.session_state.category:
    st.markdown("<h3>🍿🔥Guess the Movie Before the Popcorn Burns!</h3>", unsafe_allow_html=True)
    st.markdown("<h5>🎥 Lights, Camera, Guess</h5>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)


# --- Category Selection ---
if not st.session_state.category:
    st.subheader("Select a Movie Industry")
    st.subheader("Choose a category 🕵️‍♀️:")

    col1, col2 = st.columns(2)

    if col1.button("Bollywood and Tollywood 🎬💃🎤"):
        category = "Bollywood+Tollywood"
        all_qs = get_all_quiz_questions(category)
        st.session_state.category = category
        st.session_state.all_questions = all_qs
        st.session_state.used_titles = set()
        st.session_state.question = random.choice(all_qs)
        st.rerun()

    if col2.button("Hollywood 🎞️🎭🌟"):
        category = "Hollywood"
        all_qs = get_all_quiz_questions(category)
        st.session_state.category = category
        st.session_state.all_questions = all_qs
        st.session_state.used_titles = set()
        st.session_state.question = random.choice(all_qs)
        st.rerun()

    st.stop()

# --- Game Over Message ---
if st.session_state.game_over:
    st.success("🥳 Thanks for playing, movie buff!")
    st.balloons()
    st.markdown("**Come back soon for more fun!** 🍿🎉")
    st.stop()

# --- Get the current question ---
question = st.session_state.question

# --- Handle missing question ---
if not question or "storyline" not in question or "options" not in question or "answer" not in question:
    st.error("🚨 Could not load a valid quiz question. Please try restarting the game.")
    if st.button("Restart Game 🔁"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    st.stop()

# --- Game UI ---
st.subheader("🎥 Movie Plot:")
st.markdown(
    f"""
    <div class='storyline'>
        {question['storyline']}
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("❓ Which movie is this?")
options = question["options"]

cols1 = st.columns(2)
cols2 = st.columns(2)

for i, option in enumerate(options):
    btn_label = f"{i+1}] {option}"
    if i < 2:
        if cols1[i].button(btn_label):
            st.session_state.user_answer = option
            st.session_state.show_result = True
            st.rerun()
    else:
        if cols2[i-2].button(btn_label):
            st.session_state.user_answer = option
            st.session_state.show_result = True
            st.rerun()

# --- Show Result ---
if st.session_state.show_result:
    correct = question["answer"]
    if st.session_state.user_answer == correct:
        st.success("✅ Correct! You're a true movie buff!")
    else:
        st.error(f"❌ Oops! The correct answer was **{correct}**")

# --- Navigation Buttons ---
st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

if col1.button("Next Question ➡️"):
    st.session_state.used_titles.add(st.session_state.question["answer"])

    remaining = [
        q for q in st.session_state.all_questions
        if q["answer"] not in st.session_state.used_titles
    ]

    if remaining:
        st.session_state.question = random.choice(remaining)
        st.session_state.show_result = False
        st.session_state.user_answer = None
        st.rerun()
    else:
        st.session_state.game_over = True
        st.rerun()

if col2.button("Exit Game 🚪"):
    st.session_state.game_over = True
    st.rerun()






