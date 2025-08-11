import streamlit as st
import random

st.set_page_config(page_title="Quiz rapide", page_icon="🧠", layout="centered")

st.title("🧠 Quiz rapide")
st.write("Réponds aux questions et essaie de faire le meilleur score !")

# Liste de questions et réponses
questions = [
    {"question": "Quelle est la capitale de la France ?", "options": ["Paris", "Lyon", "Marseille"], "answer": "Paris"},
    {"question": "Combien font 7 x 8 ?", "options": ["54", "56", "58"], "answer": "56"},
    {"question": "Quel langage utilisons-nous ici ?", "options": ["Python", "Java", "C++"], "answer": "Python"},
    {"question": "Combien y a-t-il de continents sur Terre ?", "options": ["5", "6", "7"], "answer": "7"},
    {"question": "Qui a créé Streamlit ?", "options": ["Google", "Streamlit Inc.", "Microsoft"], "answer": "Streamlit Inc."}
]

# Initialisation
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

# Jeu
if not st.session_state.quiz_done:
    q = questions[st.session_state.quiz_index]
    st.subheader(f"Question {st.session_state.quiz_index + 1} / {len(questions)}")
    answer = st.radio(q["question"], q["options"], key=f"q{st.session_state.quiz_index}")

    if st.button("Valider ma réponse"):
        if answer == q["answer"]:
            st.success("✅ Bonne réponse !")
            st.session_state.quiz_score += 1
        else:
            st.error(f"❌ Mauvaise réponse ! La bonne réponse était : {q['answer']}")
        st.session_state.quiz_index += 1

        if st.session_state.quiz_index >= len(questions):
            st.session_state.quiz_done = True
        else:
            st.experimental_rerun() 

else:
    st.success(f"🎉 Quiz terminé ! Ton score final est {st.session_state.quiz_score}/{len(questions)}")
    if st.button("Rejouer"):
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_done = False
        st.experimental_rerun()
