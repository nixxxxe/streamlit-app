import streamlit as st

tab1, tab2 = st.tabs(["🏠 Overview", "📚 Education & Achievements"])

with tab1:
    st.header("")
    col1, col2 = st.columns([2, 4])
    with col1:
        st.image("images/me.png", use_column_width=True)
    with col2:
        st.markdown("""
        ### Hey, there! 👋
        My name is **Marc Denisse S. Avila**, and I’m currently a 4th-year BSIT student at CIT-University. 
        I was born and raised in **Cebu City** and currently reside in Guadalupe, Cebu City.

        I'm interested in technology and am continuously learning to expand my knowledge and skills in the field. 
        In addition to my academic pursuits, I love binge-watching series or movies across various genres or immersing myself in music. 
        I also find peace in strolling around the nearby park and mall or meeting up with my friends sometimes, allowing me to relax and recharge.

        I believe in a balanced life where hard work and relaxation go hand in hand, and I'm always up for new challenges that push my limits. 
        If you want to know more about my journey, feel free to explore the other tabs.
        """)

with tab2:
    st.header("Education & Achievements")
    col1, col2 = st.columns([2,2])
    with col1:
        st.markdown("""
        ### Education
        - 🎓 Currently pursuing a Bachelor of Science in Information Technology at CIT-University
        - 🏫 Graduated from the University of Southern Philippines Foundation for High School 

        ### Achievements
        - 🏆 Graduated Senior High School With Honors 
        - 🏆 Graduated Junior High School With Honors
        - 🏆 Served as the Junior High School SSG 8th-9th Grade Representative
        """)
    with col2:
        st.image("images/bg.png", use_column_width=True)

    st.text_input("Feel free to share your thoughts:", "")
