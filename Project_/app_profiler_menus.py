import streamlit as st
import pandas as pd
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="My Digital Profile", page_icon="👤", layout="centered")

# ---------- HEADER ----------
st.title("👋 Hello, I'm Bongani Ngcongolo")
st.subheader("Physics Student | Data Analyst | Developer")

st.write("""
Welcome to my digital profile!  
Here you can learn more about me, my skills, and my projects.
""")

st.divider()

# ---------- ABOUT ME ----------
st.header("📖 About Me")
st.write("I am a BSc Physics Honours student interested in data science, programming, and renewable energy research.")

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
BSc(hons) Physics (UWC) - In progress
BSc Physics (UWC) - Completed in 2025

""")

# ---------- PROJECTS ----------
st.header("📂 Projects")

st.write("**Project 1: Salary Data Analysis**")
st.write("""
Analysing the salary distribution for different departments to determine the business model used by the company to pay monthly salaries.
This project focuses on determining the business model that is used in this company to fairly allocate monthly salaries to employees.
There are no specific factors that the company has specified as their criteria in allocating the salaries, so we will carefully clean, 
analyse, extract information, visualize trends and predict salaries.
""")

st.write("**Project 2:  product usage and user engagement evaluation**")
st.write("""
Conducted an end-to-end analysis of product usage and user engagement data to evaluate customer behavior, retention, and monetization patterns. 
Cleaned and transformed messy event-level data, engineered time-based features, and handled missing values using group-level statistical 
imputation. Analyzed session behavior, active user trends, revenue tiers, and engagement timing to identify high-value users and early churn 
signals. Delivered actionable insights through exploratory data analysis, segmentation, and visualizations to support product and growth decision-making.
""")

# ---------- EXPERIENCE ----------
st.header("💼 Experience")
st.write("""
**Second year mathematics tutor**  
University of the Western cape
     
Job title, Second year Mathematics tutor at the University of the Western Cape responsible for Helping students with Linear Algebra, Algebraic structures, Advanced 
calculus and Vector Calculus. I also helped with marking tutorials, assignmentsand verifying marks. 
""")

# ---------- CONTACT ----------
st.header("📬 Contact Me")

st.write("📧 Email: ngcongolobongani982@gmail.com")
st.write("💼 LinkedIn: https://www.linkedin.com/in/bongani-ngcongolo-056917248/")
st.write("🐙 GitHub: https://github.com/BonganiNgcongolo")

st.divider()

st.write("© 2026 [Bongani Ngcongolo] — Built with Streamlit")



