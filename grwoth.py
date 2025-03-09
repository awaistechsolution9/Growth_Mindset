import streamlit as st
import random
import datetime
import time
import openai 
import streamlit_antd_components as sac
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_lottie import st_lottie
import json

# Page Configuration
st.set_page_config(page_title="🌱 Growth Mindset Hub", page_icon="🔥", layout="wide")

# Custom CSS for Advanced UI
st.markdown("""
    <style>
    body { background-color: #0D0D2B; color: #ffffff; font-family: 'Poppins', sans-serif; }
    .stButton button { 
        background: linear-gradient(135deg, #ff7eb3, #ff758c);
        color: white; border-radius: 15px;
        padding: 12px 25px; font-size: 16px;
        transition: all 0.3s ease-in-out;
        border: 2px solid transparent;
        animation: neon-glow 1.5s infinite alternate;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 5px 15px rgba(255, 118, 136, 0.6);
    }
    @keyframes neon-glow {
        from { border-color: rgba(255, 118, 136, 0.4); }
        to { border-color: rgba(255, 118, 136, 0.8); }
    }
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 30px rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .stTextInput>div>div>input,
    .stTextArea>div>textarea {
        background-color: rgba(255, 255, 255, 0.1);
        color: black;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://media.istockphoto.com/id/1345793778/vector/bar-graph-growth-and-up-arrow.jpg?s=612x612&w=0&k=20&c=s3MbVY25Vrb8YcOpdwaRNYIzVR6aI35aY9dnMKQS46Q=", use_column_width=True)
    st.title("🌟 Growth Mindset Hub")
    st.markdown("---")
    page = sac.menu(["🏠 Home", "🎯 Goals", "📊 Progress", "🧠 Mindset Quiz", "📚 Resources"], format_func="title")

# AI-Powered Motivational Quote Generator
def generate_motivational_quote():
    return random.choice([
        "🌱 Mistakes help me learn and improve.",
        "🔥 Challenges help me grow stronger.",
        "🚀 Failure is just another step towards success.",
        "💡 Learning never stops!",
        "✨ Every challenge is an opportunity.",
        "🌿 Keep pushing, keep growing!",
        "💪 You are capable of amazing things!"
    ])

if page == "🏠 Home":
    st.title("🌱 Welcome to the Growth Mindset Hub")
    st.subheader("💡 Daily Motivation:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Get a New Quote 🎯"):
            st.success(generate_motivational_quote())

    with col2:
        st_lottie("https://assets6.lottiefiles.com/packages/lf20_m6cuL6.json", height=150)

    st.markdown("---")
    st.subheader("📌 Growth Mindset Principles")
    st.markdown("""
    - 🌟 **Embrace Challenges** – Every difficulty makes you stronger.
    - 📈 **Learn from Mistakes** – Feedback is the key to success.
    - 🔥 **Persist Through Setbacks** – Never give up!
    - 🌿 **Celebrate Others’ Success** – Learn from and get inspired by others.
    - 🚀 **Effort Leads to Mastery** – Practice makes progress.
    """)

if page == "🎯 Goals":
    st.title("🎯 Set & Track Your Goals")
    goal = st.text_input("Write your personal growth goal:")
    if goal:
        st.success(f"✅ Your goal: *{goal}* has been saved!")

if page == "📊 Progress":
    st.title("📊 Track Your Progress")
    st.write("Mark your completed growth activities:")

    progress_tasks = {
        "📖 Read a book on personal growth": False,
        "🎓 Learn a new skill this week": False,
        "🧘 Practice mindfulness daily": False,
        "🎯 Take on a new challenge": False
    }

    completed_count = 0
    total_tasks = len(progress_tasks)

    for task in progress_tasks.keys():
        if st.checkbox(task):
            completed_count += 1

    # Progress Bar Animation
    progress = int((completed_count / total_tasks) * 100) if total_tasks > 0 else 0
    st.progress(progress)
    st.metric(label="🔥 Your Progress", value=f"{progress}%")
    style_metric_cards()

if page == "🧠 Mindset Quiz":
    st.title("🧠 Growth Mindset Quiz")
    st.write("Test your mindset with a quick quiz!")

    questions = {
        "1️⃣ How do you handle failure?": ["I quit", "I learn from it", "I ignore it"],
        "2️⃣ What do you think about challenges?": ["I avoid them", "I embrace them", "I feel nervous"],
        "3️⃣ Do you believe intelligence is fixed?": ["Yes", "No", "Maybe"]
    }

    score = 0
    for question, options in questions.items():
        response = st.radio(question, options)
        if response in ["I learn from it", "I embrace them", "No"]:
            score += 1

    if st.button("Check Score"):
        if score == len(questions):
            st.success("🚀 You have a strong Growth Mindset!")
        elif score > 0:
            st.info("🌟 You're on your way to a Growth Mindset!")
        else:
            st.warning("💡 Keep learning and growing!")

if page == "📚 Resources":
    st.title("📚 Best Growth Mindset Resources")
    st.markdown("""
    - 📖 [Mindset: The New Psychology of Success](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)
    - 📖 [Atomic Habits](https://www.amazon.com/Atomic-Habits-Proven-Build-Break/dp/0735211299)
    - 🌐 [Learning How to Learn (Coursera)](https://www.coursera.org/learn/learning-how-to-learn)
    """)

st.info("🚀 Keep learning and growing every day!")