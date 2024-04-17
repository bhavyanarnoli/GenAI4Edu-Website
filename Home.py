import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='Home'
)

st.write('# Welcome to GenAi4Edu Helper')
st.markdown(
    """
  Welcome to our AI-powered educational assistant! Tailored to support both students and teachers, our chatbot is fine-tuned on NCERT books from classes 1 to 8. Students can ask questions, clarify doubts, and explore concepts, while teachers can effortlessly generate lesson plans aligned with curriculum standards. Revolutionize your learning and teaching experience with our intuitive chatbot today!
"""
)