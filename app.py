import streamlit as st
import time
import difflib
import random

# Sample paragraphs
paragraphs = [
    "The quick brown fox jumps over the lazy dog. Typing tests help improve speed and accuracy.",
    "Streamlit makes it easy to build web apps for machine learning and data science.",
    "Practice typing regularly to improve your speed, accuracy, and confidence on the keyboard.",
    "Consistent effort and smart work lead to success in both academic and personal life.",
    "Technology is best when it brings people together and solves real-world problems."
]

st.set_page_config(page_title="Typing Speed Test", layout="centered")

st.title("⌨️ Typing Speed Test")

# Initial setup
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'current_para' not in st.session_state:
    st.session_state.current_para = random.choice(paragraphs)
if 'test_completed' not in st.session_state:
    st.session_state.test_completed = False

# Display the paragraph
st.markdown("### Type the following paragraph:")
st.markdown(f"""
<div style="border-radius: 10px; padding: 20px; background: #e0f7fa; color: #000; font-size: 18px; line-height: 1.6;">
{st.session_state.current_para}
</div>
""", unsafe_allow_html=True)

# Typing area
typed_text = st.text_area("Start typing here...", height=150)

# Start timer
if st.session_state.start_time is None and typed_text:
    st.session_state.start_time = time.time()

# Submit button
if st.button("✅ Submit"):
    if typed_text.strip():
        end_time = time.time()
        elapsed_time = end_time - st.session_state.start_time
        words_typed = len(typed_text.strip().split())
        wpm = round(words_typed / (elapsed_time / 60))

        # Accuracy calculation
        matcher = difflib.SequenceMatcher(None, st.session_state.current_para, typed_text)
        accuracy = round(matcher.ratio() * 100, 2)

        st.success(f"⏱ Time: {round(elapsed_time, 2)} sec | 💬 WPM: {wpm} | 🎯 Accuracy: {accuracy}%")

        # Highlight differences
        def highlight_diff(expected, actual):
            result = ""
            matcher = difflib.SequenceMatcher(None, expected, actual)
            for opcode, i1, i2, j1, j2 in matcher.get_opcodes():
                if opcode == 'equal':
                    result += f"<span style='color:green'>{actual[j1:j2]}</span>"
                else:
                    result += f"<span style='color:red'>{actual[j1:j2]}</span>"
            return result

        st.markdown("### 🔍 Comparison:")
        html_diff = highlight_diff(st.session_state.current_para, typed_text)
        st.markdown(f"<div style='border:1px solid #ccc; padding:10px'>{html_diff}</div>", unsafe_allow_html=True)

        st.session_state.test_completed = True

# Restart Button
if st.session_state.test_completed:
    if st.button("🔁 Restart"):
        st.session_state.start_time = None
        st.session_state.current_para = random.choice(paragraphs)
        st.session_state.test_completed = False
        st.rerun()
else:
    st.info("Start typing to begin the test and click Submit when done.")
