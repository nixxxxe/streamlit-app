import streamlit as st

# Define columns
col1, col2, col3 = st.columns(3)

# Project 1
with col1:
    st.image("images/sppec.png", caption="Project 1", use_column_width=True)
    st.markdown("""
    **Project 1: SpecSavvy**
    - **Description**: This UI/UX project involves creating an app that helps non-tech-savvy individuals understand 
      product specifications, enabling them to make informed purchasing decisions.
    - **Technologies used**: Figma.
    - [View Project](https://www.figma.com/proto/IGLq1wqxAB9PrpX0l5gzk4/Spec-Savvy?)
    """)

# Project 2
with col2:
    st.image("images/nexxa.png", caption="Project 2", use_column_width=True)
    st.markdown("""
    **Project 2: Nexa-Ai**
    - **Description**: Nexa-Ai is an AI chatbot powered by Azure OpenAI services, capable of reading PDFs.
    - **Technologies used**: Streamlit, Azure OpenAI's API.
    - [View Project](https://github.com/hanako0311/Nexa-Ai.git)
    """)

# Project 3
with col3:
    st.image("images/findnest.png", caption="Project 3", use_column_width=True)
    st.markdown("""
    **Project 3: FindNest**
    - **Description**: FindNest is an innovative digital solution designed to streamline and enhance the lost and found process 
      at CIT-University.
    - **Technologies used**: React with vite, Node.js, Express.js, MongoDB.
    - [View Project](https://github.com/hanako0311/FindNest.git)
    """)
