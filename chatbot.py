import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Tutor",
    page_icon="🎓",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#2E86C1;
}
.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown("<div class='main-title'>🎓 AI Tutor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Learn Concepts Step-by-Step with AI</div>", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.header("📚 Study Tips")

    st.info("""
    ✔ Ask one question at a time.

    ✔ Request examples.

    ✔ Ask for step-by-step explanations.

    ✔ Ask for quizzes after learning.

    ✔ Don't hesitate to ask follow-up questions.
    """)

    st.divider()

    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# -------------------------
# Model
# -------------------------
model = ChatMistralAI(
    model_name="mistral-small-2506",
    MISTRAL_API_KEY='ax6xjnejKqHVupYcbVSab8Q583yaLTuV',
    temperature=0.7,
)

# -------------------------
# Prompt Template
# -------------------------
prompt = ChatPromptTemplate.from_template("""
You are an experienced AI Tutor.

Your goal is to help students understand concepts rather than simply giving answers.

Guidelines:
- Explain concepts in simple language.
- Teach step by step.
- Encourage critical thinking.
- If the student is wrong, politely correct them.
- Give examples whenever helpful.
- If the student asks for code, explain the logic before showing the code.
- If the question is mathematical, show all calculation steps.
- Keep responses concise unless the student asks for more detail.
- End your answer by asking a follow-up question to check understanding.

Student Question:
{question}
""")

# -------------------------
# Chat History
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"👋 Hello! I'm your AI Tutor.\n\nAsk me anything about programming, mathematics, science, cybersecurity, AI, or any other subject."
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# Chat Input
# -------------------------
user_question = st.chat_input("Ask your question here...")

if user_question:

    # User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    # Generate Response
    with st.chat_message("assistant"):

        with st.spinner("🧠 Tutor is thinking..."):

            final_prompt = prompt.invoke(
                {
                    "question":user_question
                }
            )

            response = model.invoke(final_prompt)

            st.markdown(response.content)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response.content
        }
    )