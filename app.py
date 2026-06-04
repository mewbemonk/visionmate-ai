import streamlit as st

from webcam.frame import webcam
from memory.context import get_context
from agents.questions_agent import questions
from agents.search_agent import search_agent
from speech_to_text.listen import listen
from text_to_speech.pyttsx import voice


st.set_page_config(
    page_title="VisionMate AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------
# Session State
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------
# Header
# -----------------------

st.title("🤖 VisionMate AI")
st.caption(
    "Scan objects • Understand products • Ask questions by voice"
)

st.divider()

# -----------------------
# Main Layout
# -----------------------

left, right = st.columns([1, 1])

# =======================
# LEFT PANEL
# =======================

with left:

    st.subheader("📷 Object Scanner")

    if st.button(
        "Start Scan",
        use_container_width=True
    ):

        with st.spinner(
            "Scanning object..."
        ):

            webcam()

        st.success(
            "Object scanned successfully."
        )

# =======================
# RIGHT PANEL
# =======================

with right:

    st.subheader("🧠 Detected Information")

    context = get_context()

    st.text_area(
        "Context",
        value=context,
        height=250,
        disabled=True
    )

st.divider()

# -----------------------
# Voice Assistant
# -----------------------

st.subheader("🎤 Voice Assistant")

if st.button(
    "Ask By Voice",
    use_container_width=True
):

    with st.spinner(
        "Listening..."
    ):

        question = listen()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner(
        "Thinking..."
    ):

        answer = questions(
            get_context(),
            question
        )

        if answer == "SEARCH_REQUIRED":

            answer = search_agent(
                get_context(),
                question
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    voice(answer)

# -----------------------
# Conversation
# -----------------------

st.subheader("💬 Conversation")

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])