import streamlit as st

# Define some example products
products = {
    "1": {"name": "Womens Dress", "price": 39.99, "image": "https://cdn.pixabay.com/photo/2016/11/29/13/32/attractive-1868750_960_720.jpg"},
    "2": {"name": "Mens Shirt", "price": 24.99, "image": "https://cdn.pixabay.com/photo/2018/10/29/18/05/woman-3784052_960_720.jpg"},
    "3": {"name": "Womens Jacket", "price": 59.99, "image": "https://cdn.pixabay.com/photo/2016/02/19/11/25/model-1209787_960_720.jpg"}
}

# Define the shopping cart as a dictionary of product ids and quantities
cart = {}

# Header section
st.write("<h1 style='text-align: center;'>Shopping Cart</h1>", unsafe_allow_html=True)
st.write("<hr>", unsafe_allow_html=True)

# Shopping cart section
with st.container():
    st.header("Your Shopping Cart")
    st.write("<p style='text-align: center;'>Here are the items in your cart:</p>", unsafe_allow_html=True)
    
    if not cart:
        st.write("<p style='text-align: center;'>Your cart is empty.</p>", unsafe_allow_html=True)
    else:
        total_price = 0
        for product_id, quantity in cart.items():
            product = products[product_id]
            price = product["price"] * quantity
            total_price += price
            
            col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
            
            with col1:
                st.image(product["image"], use_column_width=True)
            
            with col2:
                st.write(f"<h3>{product['name']}</h3>", unsafe_allow_html=True)
                st.write(f"<p>Price: ${product['price']}<br>Quantity: {quantity}</p>", unsafe_allow_html=True)
            
            with col3:
                st.write(f"<p>Subtotal: ${price:.2f}</p>", unsafe_allow_html=True)
            
            with col4:
                if st.button(f"Remove {product['name']}"):
                    del cart[product_id]
        
        st.write("<hr>", unsafe_allow_html=True)
        st.write(f"<p style='text-align: right;'>Total: ${total_price:.2f}</p>", unsafe_allow_html=True)

# Continue shopping button
st.write("<hr>", unsafe_allow_html=True)
if st.button("Continue Shopping"):
    st.write("Redirect to shopping page here...")

