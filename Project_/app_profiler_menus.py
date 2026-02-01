import streamlit as st
import pandas as pd
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="My Digital Profile", page_icon="👤", layout="centered")

# ---------- HEADER ----------
st.title("👋 Hello, I'm [Your Name]")
st.subheader("Physics Student | Data Analyst | Developer")

st.write("""
Welcome to my digital profile!  
Here you can learn more about me, my skills, and my projects.
""")

st.divider()

# ---------- ABOUT ME ----------
st.header("📖 About Me")
st.write("
I am a BSc Physics Honours student interested in data science, programming, and renewable energy research.
")

# ---------- SKILLS ----------
st.header("🛠️ Skills")
skills = [
    "Python",
    "Data Analysis",
    "Machine Learning",
    "HTML & CSS",
    "SQL",
    "Research"
]

for skill in skills:
    st.write(f"- {skill}")

# ---------- EDUCATION ----------
st.header("🎓 Education")
st.write("""
**[BSc(hons) Physics (UWC) - In progress]**  
[BSc Physics (UWC) - Completed in 2025]  

""")

# ---------- PROJECTS ----------
st.header("📂 Projects")

st.write("**Project 1: [Project Name]**")
st.write("""
Short description of the project.
What problem it solves and what tools you used.
""")

st.write("**Project 2: [Project Name]**")
st.write("""
Short description of the project.
""")

# ---------- EXPERIENCE ----------
st.header("💼 Experience")
st.write("""
**[Job/Internship/Volunteer Role]**  
[Organization]  
[What you did]
""")

# ---------- CONTACT ----------
st.header("📬 Contact Me")

st.write("📧 Email: ngcongolobongani982@gmail.com")
st.write("💼 LinkedIn: https://www.linkedin.com/in/bongani-ngcongolo-056917248/")
st.write("🐙 GitHub: https://github.com/BonganiNgcongolo")

st.divider()

st.write("© 2026 [Bongani Ngcongolo] — Built with Streamlit")
