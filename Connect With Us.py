import streamlit as st
import csv

def main():
    st.set_page_config(page_title="Sign up for our newsletter", page_icon="📰", layout="wide")
    st.write("# Sign up for our newsletter")
    st.write("Enter your information below to receive news and updates about our products, as well as a 10% discount on your next purchase!")
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    email = st.text_input("Email address")
    subscribe = st.button("Subscribe")

    if subscribe:
        # Save user data to CSV file
        with open('subscribers.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([first_name, last_name, email])
        # Show confirmation message
        st.write("Thank you for subscribing to our newsletter!")
        st.write("Your discount code is: **NEWS10**")

if __name__ == "__main__":
    main()
