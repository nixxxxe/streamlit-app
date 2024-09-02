import streamlit as st

# Skills Section
st.markdown("""
### Skills
- 🖥️ Programming languages: JavaScript, Python
- 🌐 Web Development: HTML, CSS, React
""")

# Contact Me Section
st.subheader("Contact Me")
st.write("Feel free to reach out for collaboration or freelance work:")

# Contact Form
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    agree = st.checkbox("I consent to having this website store my submitted information so they can respond to my inquiry.")

    submit_button = st.form_submit_button("Submit")

    if submit_button and agree:
        st.success(f"Thank you for reaching out, {name}! I will get back to you at {email} soon.")
    elif submit_button and not agree:
        st.error("You need to agree to the consent checkbox before submitting.")

# Direct Contact Links
st.markdown("""
### Or, reach out to me directly:
- 📧 Email: [marcdenisse.avila](mailto:marcdenisse.avila@cit.edu)
""")
