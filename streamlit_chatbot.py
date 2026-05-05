import os
import streamlit as st

try:
    import openai
    openai_available = True
except ImportError:
    openai_available = False


def get_ai_response(message, api_key, model="gpt-3.5-turbo"):
    if not openai_available:
        return "Error: openai package not installed. Install with 'pip install openai'."

    api_key = api_key or os.environ.get("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")
    if not api_key:
        return "Please provide a valid OpenAI API key in the sidebar or OPENAI_API_KEY environment variable."

    openai.api_key = api_key

    # Enhance response for news requests
    system_prompt = (
        "You are an intelligent assistant with access to current news stories. "
        "When the user asks about news, provide top headlines and short summaries in bullet points. "
        "If you cannot access live data, generate a realistic news-style summary around current events. "
        "Always return concise, helpful text."
    )

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message},
            ],
            temperature=0.7,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI response error: {e}"


def get_bot_response(user_message):
    message = user_message.strip().lower()
    if not message:
        return "Please say something so I can respond."
    if "hello" in message or "hi" in message:
        return "Hello! I am your easy Streamlit assistant. How can I help today?"
    if "help" in message:
        return "You can ask me about features, UI, or just chat about your day."
    if "bye" in message or "goodbye" in message:
        return "Goodbye! Have an awesome day!"
    if "thanks" in message or "thank you" in message:
        return "You’re welcome! Anything else I can do for you?"
    return "Nice to hear from you! I’m a demo chatbot; try typing 'help', 'hello', or 'bye'."


def render_message(speaker, text):
    if speaker == "You":
        color = "#007bff"
        align = "flex-end"
        text_color = "white"
    else:
        color = "#f1f3f5"
        align = "flex-start"
        text_color = "#212529"

    bubble = (
        f"<div style='display:flex;justify-content:{align};margin:6px 0;'>"
        f"<div style='max-width:82%;background:{color};color:{text_color};border-radius:16px;padding:10px 14px;box-shadow:0 2px 6px rgba(0,0,0,0.14);'>"
        f"<strong>{speaker}:</strong> {text}</div></div>"
    )
    st.markdown(bubble, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Streamlit Real-Time AI Chat", page_icon="🤖", layout="wide")

    st.markdown("""
    <style>
        .page-background { background: linear-gradient(135deg, #1f4068, #00b7ff); min-height: 100vh; padding: 18px; border-radius: 20px; }
        .title-white { color: #ffffff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .subtitle { color: #d0e7ff; }
        .stTextInput > div > div > input { background: #ffffffcc !important; border: 1px solid #ced4da !important; }
        .stButton button { background: #28a745; color: #fff; border: none; }
        .stButton button:hover { background: #218838; }
        .api-info { color: #fff; font-size: 0.9em; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='page-background'><h1 class='title-white'>Streamlit AI Chat (Real-time UX)</h1><p class='subtitle'>Enter your OpenAI API key and message to chat with AI.</p></div>", unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []

    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

    if "api_key" not in st.session_state:
        st.session_state.api_key = "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"

    if "model" not in st.session_state:
        st.session_state.model = "gpt-3.5-turbo"

    with st.sidebar:
        st.header("AI Settings")
        st.session_state.api_key = st.text_input("OpenAI API Key", value=st.session_state.api_key, type="password", placeholder="sk-...")
        st.session_state.model = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4"], index=0)
        if not openai_available:
            st.error("Install the openai package: pip install openai")

    chat_box = st.container()

    with st.form(key="chat_form", clear_on_submit=True):
        st.text_input("Your message", key="input_text", placeholder="Write your message here...", label_visibility="collapsed")
        submit = st.form_submit_button("Send")

    if submit and st.session_state.input_text.strip():
        user_msg = st.session_state.input_text.strip()
        st.session_state.history.append(("You", user_msg))

        # Always use OpenAI path, but provide a clear error if key is missing.
        ai_text = get_ai_response(user_msg, st.session_state.api_key, st.session_state.model)

        # If API key isn't set, get_ai_response returns a user-readable message.
        st.session_state.history.append(("Bot", ai_text))
        # No manual reset of st.session_state.input_text here; clear_on_submit=True already handles it

    with chat_box:
        for speaker, text in st.session_state.history:
            render_message(speaker, text)

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Clear chat"):
            st.session_state.history = []
    with col2:
        st.markdown("<p class='api-info'>Tip: For real-time feel, use short messages and keep the model prompt concise.</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()