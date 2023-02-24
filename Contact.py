import streamlit as st

def app():
    st.title("Contact Us")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button(label='Submit')

        if submit:
            # Code to send email or save form data to database goes here
            st.success("Thank you for your message! We will get back to you soon.")
app()