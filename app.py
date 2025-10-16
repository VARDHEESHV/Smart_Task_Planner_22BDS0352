import streamlit as st
import planner
import os

st.set_page_config(
    page_title="Smart Task Planner",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    .stTextInput>div>div>input {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0.5rem;
        border: 1px solid #007bff;
        background-color: #007bff;
        color: white;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border-color: #0056b3;
        color: white;
    }
    h1, h3 {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://placehold.co/400x200/007bff/FFFFFF?text=Smart+Planner&font=inter", use_column_width=True)
    st.info("This app uses the Gemini API to break down your goals into actionable tasks. Enter your goal and get a detailed plan with timelines and dependencies.")

st.title("✅ Smart Task Planner")
st.markdown("Turn your ambitious goals into a step-by-step plan. Let AI do the heavy lifting!")

goal = st.text_area(
    "Enter your goal:",
    height=150,
    placeholder="e.g., 'Launch a new podcast about AI in 30 days' or 'Learn Python for data analysis in 3 months'"
)

if st.button("Generate Plan"):
    if not goal:
        st.error("⚠️ Please enter a goal to generate a plan.")
    else:
        try:
            with st.spinner("🤖 Generating your actionable plan... Please wait."):
                plan = planner.generate_plan(user_goal=goal)

            st.success("🚀 Your plan is ready!")
            st.markdown("---")
            st.markdown(plan)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("There might be an issue with the backend or the API key.")

st.markdown("---")
st.header("How to Use")
st.markdown("""
1.  **Define your Goal:** Write a clear and concise goal in the text area.
2.  **Generate:** Click the "Generate Plan" button and watch the magic happen!
""")