import streamlit as st
import random

# 🖥️ Page config
st.set_page_config(page_title="Ideal Self AI", page_icon="🧠", layout="centered")

# 🎨 UI Styling
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
h1 {
    font-size: 42px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Ideal Self AI")
st.caption("Think clearly. Act wisely. Become your best self.")

# 🔒 Expanded privacy keywords
sensitive_keywords = [
    "phone", "number", "address", "bank", "password",
    "otp", "email", "location", "photo", "video",
    "aadhaar", "pan", "personal", "private", "details"
]

# 🧠 Emotion detection
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["confused", "lost", "uncertain"]):
        return "confusion"
    elif any(word in text for word in ["angry", "frustrated"]):
        return "frustration"
    elif any(word in text for word in ["sad", "hurt"]):
        return "sadness"
    elif any(word in text for word in ["fear", "scared"]):
        return "fear"
    else:
        return "mixed"

# 🔒 Privacy responses (5 variations)
privacy_responses = [
    "Sharing personal information online can expose you to risks you may not immediately see.",
    "Even if it feels safe, once personal details are shared, you lose control over them.",
    "Online spaces are not always secure, and personal information can be misused.",
    "It may seem harmless now, but sharing private details can lead to long-term risks.",
    "Your safety matters more than convenience — not everything should be shared online."
]

privacy_actions = [
    "Avoid sharing any sensitive information unless absolutely necessary.",
    "Pause and rethink before sharing anything personal online.",
    "Keep your personal details private and protected.",
    "Limit what you share — especially in uncertain environments.",
    "Choose safety over impulse when it comes to personal data."
]

privacy_reflect = [
    "Would you be comfortable if this information became public?",
    "Is sharing this truly necessary right now?",
    "What could go wrong if this information is misused?",
    "Are you trusting the right platform or person?",
    "Is there a safer way to handle this situation?"
]

# 🧠 Normal responses (variations)
emotion_lines = {
    "confusion": [
        "You seem to be feeling uncertain, which often happens when too many thoughts overlap.",
        "Confusion usually means you're trying to process something important without clarity."
    ],
    "frustration": [
        "There’s frustration here, likely from things not going as expected.",
        "This feels like emotional tension building up from repeated challenges."
    ],
    "fear": [
        "This sounds like fear, which often amplifies worst-case scenarios.",
        "You may be focusing more on what could go wrong than what you can control."
    ],
    "sadness": [
        "There’s emotional heaviness here, and it’s important to acknowledge it.",
        "This feels like sadness, which can cloud decision-making."
    ],
    "mixed": [
        "There are multiple thoughts and emotions involved here.",
        "Your mind seems divided, which can reduce clarity."
    ]
}

perspectives = [
    "Your future self would slow down and respond with clarity, not impulse.",
    "A wiser version of you would step back before making any decision.",
    "Clarity comes when you pause instead of reacting immediately.",
    "Your ideal self would think long-term, not just react to the moment.",
    "Better decisions come from calm thinking, not emotional urgency."
]

actions = [
    "Take a short pause and write down what is actually in your control.",
    "Give yourself space before making a decision.",
    "Focus on one small step instead of everything at once.",
    "Detach from the emotion and observe the situation clearly.",
    "Slow down — clarity improves when you don’t rush."
]

reflect_questions = [
    "What would your best version do differently right now?",
    "Are you reacting, or are you thinking clearly?",
    "Will this decision matter in the long term?",
    "What is truly in your control here?",
    "If you were calm, how would you respond?"
]

# 🧠 Response generator
def generate_response(user_input):
    text = user_input.lower()

    # 🔒 Privacy detection (strong)
    if any(word in text for word in sensitive_keywords) or "share" in text:
        return f"""
⚠️ **Pause — This Could Be Risky**

{random.choice(privacy_responses)}

Your wiser self would not act on impulse here — they would protect their boundaries first.

👉 **Action:** {random.choice(privacy_actions)}

💭 **Think:** {random.choice(privacy_reflect)}
"""

    # 🧠 Normal flow
    emotion = detect_emotion(user_input)

    return f"""
**You said:** "{user_input}"

---

🧠 **Understanding You**  
{random.choice(emotion_lines[emotion])}

---

🌱 **A Better Perspective**  
{random.choice(perspectives)}

---

⚡ **What You Can Do Next**  
{random.choice(actions)}

---

💭 **Think About This**  
{random.choice(reflect_questions)}
"""

# 📝 Input
user_input = st.text_input("What's on your mind?")

if user_input:
    if any(word in user_input.lower() for word in sensitive_keywords):
        st.warning("⚠️ Avoid sharing sensitive personal information.")

    with st.spinner("Thinking..."):
        st.write("")

    reply = generate_response(user_input)

    st.markdown("### 🧘 Your Ideal Self says:")
    st.markdown(reply)