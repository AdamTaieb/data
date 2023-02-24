import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit_lottie



st.set_page_config(page_title="Clothing Retailer", page_icon="👕", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets
lottie_clothes = load_lottie("https://assets2.lottiefiles.com/packages/lf20_gn0tojcq.json")

# Header Section
with st.container():
    st.subheader("Welcome to our Clothing Store!")
    st.title("We have the perfect outfit for you!")
    st.write("[Shop now](http://localhost:8501/Shop)")

# Section 2
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Offer")
        st.write("##")
        st.write(
            """
            We offer a wide variety of clothing for all occasions, including:

            - Casual wear
            - Work attire
            - Formal wear
            - Athletic apparel

            We pride ourselves on providing high-quality, stylish clothing at affordable prices. Come shop with us today!
            """
        )
    st.write("[View Our Collection](http://localhost:8501/Shop)")
 
    with right_column:
        st_lottie(lottie_clothes, height=300, key="clothing")


# Section 4 - Latest Arrivals

# Product Section
with st.container():
    st.write("---")
    st.header("New Arrivals")
    st.write("##")
    st.write("<p style='text-align: center;'>Check out our latest collection of clothes that just arrived. Don't miss out on the chance to be the first to wear our newest pieces.</p>", unsafe_allow_html=True)
    
    # Display product cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://cdn.pixabay.com/photo/2016/11/29/13/32/attractive-1868750_960_720.jpg", use_column_width=True)
        st.write("<h3 style='text-align: center;'>Womens Dress</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;'>$39.99</p>", unsafe_allow_html=True)
        if st.button("Add to Cart 1"):
            st.write("Item 1 added to cart!")
        
    with col2:
        st.image("https://cdn.pixabay.com/photo/2018/10/29/18/05/woman-3784052_960_720.jpg", use_column_width=True)
        st.write("<h3 style='text-align: center;'>Mens Shirt</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;'>$24.99</p>", unsafe_allow_html=True)
        if st.button("Add to Cart 2"):
            st.write("Item 2 added to cart!")
        
    with col3:
        st.image("https://cdn.pixabay.com/photo/2016/02/19/11/25/model-1209787_960_720.jpg", use_column_width=True)
        st.write("<h3 style='text-align: center;'>Womens Jacket</h3>", unsafe_allow_html=True)
        st.write("<p style='text-align: center;'>$59.99</p>", unsafe_allow_html=True)
        if st.button("Add to Cart 3"):
            st.write("Item 3 added to cart!")

# Section 3
with st.container():
    st.write("---")
    st.header("Customer Reviews")
    st.write(
        """
        Don't just take our word for it - hear from our satisfied customers!

        - "I absolutely love this store! They have the best selection of clothes and the prices can't be beat." - Sarah, 28
        - "I always find what I'm looking for here. The staff is so helpful and friendly." - John, 42
        - "I was blown away by the quality of the clothes I received. Will definitely be shopping here again." - Emily, 19
        """
    )


# About Us Section
with st.container():
    st.write("---")
    st.header("About Us")
    st.write("##")
    st.write("<p style='text-align: center;'>Our brand is dedicated to providing high-quality clothing for our customers. We believe that fashion should not only be stylish, but also comfortable and affordable. Our team of designers and stylists work hard to create unique pieces that you won't find anywhere else.</p>", unsafe_allow_html=True)
    st.image("https://cdn.pixabay.com/photo/2017/07/31/17/45/fashion-2564527_960_720.jpg", use_column_width=True)


with st.container():
    st.write("---")
    st.header("Connect with us")
    st.write("##")
    st.write("<p style='text-align: center;'>Stay in touch with us and get updates on our latest collections, sales, and promotions.</p>", unsafe_allow_html=True)

    # Add links
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("<p style='text-align: center;'><a href='http://localhost:8501/Terms_and_Policies'>Terms and Policies</a></p>", unsafe_allow_html=True)

    with col2:
        st.write("<p style='text-align: center;'><a href='http://localhost:8501/Contact'>Contact Us</a></p>", unsafe_allow_html=True)

    with col3:
        st.write("<p style='text-align: center;'><a href='https://twitter.com/example'>Follow us on Twitter</a></p>", unsafe_allow_html=True)

    # Add horizontal line
    st.write("<hr>", unsafe_allow_html=True)
