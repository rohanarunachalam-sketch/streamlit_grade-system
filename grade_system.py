import html
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Grade System",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 5px;
        color: #FFFFFF;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
        color: #FFFFFF;
    }
    .result-card {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 25px;
        border: 1px solid #ddd;
        color: #000000;
    }
    .student-name {
        font-size: 28px;
        font-weight: bold;
        color: #000000;
    }
    .score {
        font-size: 24px;
        margin-top: 10px;
        color: #000000;
    }
    .grade {
        font-size: 70px;
        font-weight: bold;
        margin: 10px;
        color: #000000;
    }
    .quote {
        font-size: 20px;
        font-style: italic;
        margin-top: 15px;
        color: #000000;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 15px;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🎓 Student Grade System</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Discover your result and keep moving forward 🚀</div>',
    unsafe_allow_html=True
)

# Student name
name = st.text_input(
    "👤 Enter your name",
    placeholder="Example: Rohan"
)

# Mark
mark = st.number_input(
    "📝 Enter your mark",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=1.0
)

# Progress bar (uses exact mark, not truncated)
st.progress(min(mark / 100, 1.0))

# Calculate button
if st.button("✨ Calculate My Grade", use_container_width=True):
    if not name.strip():
        st.warning("⚠️ Please enter your name first.")
    else:
        # Escape name to prevent HTML injection
        safe_name = html.escape(name.strip())

        # Grade calculation
        if mark >= 90:
            grade = "A"
            emoji = "🏆"
            card_color = "#e6f9ed"
            border_color = "#34c759"
            quote = (
                "Excellent work! Your dedication is turning "
                "your dreams into reality."
            )
        elif mark >= 80:
            grade = "B"
            emoji = "🌟"
            card_color = "#eaf7e9"
            border_color = "#7ac74f"
            quote = (
                "Great job! Keep pushing yourself "
                "and you can reach the top."
            )
        elif mark >= 70:
            grade = "C"
            emoji = "⭐"
            card_color = "#fff8e1"
            border_color = "#f4c542"
            quote = (
                "Good effort! Believe in yourself "
                "and keep improving every day."
            )
        elif mark >= 60:
            grade = "D"
            emoji = "💪"
            card_color = "#fff1e0"
            border_color = "#ff9f43"
            quote = (
                "You are getting there! Learn from your "
                "mistakes and keep moving forward."
            )
        else:
            grade = "F"
            emoji = "❤️"
            card_color = "#fdecea"
            border_color = "#ff6b6b"
            quote = (
                "Don't give up! One result does not define "
                "your future. Your next chapter is waiting for you."
            )

        # Display result
        st.markdown(
            f"""
            <div class="result-card" style="background-color:{card_color}; border-color:{border_color};">
                <div class="student-name">
                    👋 {safe_name}, your score is
                </div>
                <div class="score">
                    📊 {mark} / 100
                </div>
                <div class="grade">
                    {emoji} {grade}
                </div>
                <div class="quote">
                    "{quote}"
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    '<div class="footer">'
    '💡 Every mark is a step toward your goal. '
    'Keep learning, keep growing!'
    '</div>',
    unsafe_allow_html=True
)