
import streamlit as st

# Define a dictionary containing information about the products
# Define a dictionary containing information about the products
products = {
    "T-Shirt1": {
        "name": "T-Shirt1",
        "description": "A classic fit t-shirt with a ribbed neckline. Made of 100% cotton. Comes in sizes S-XXL.",
        "price": "$20.00",
        "image": "/Users/adamtaieb/Downloads/tshirt1.png",
        "recommended": ["T-Shirt2", "T-Shirt3", "T-Shirt4"]
    },
    "T-Shirt2": {
        "name": "T-Shirt2",
        "description": "A classic fit t-shirt with a ribbed neckline. Made of 100% cotton. Comes in sizes S-XXL.",
        "price": "$20.00",
        "image": "/Users/adamtaieb/Downloads/tshirt2.png",
        "recommended": ["T-Shirt1", "T-Shirt3", "T-Shirt4"]
    },
    "T-Shirt3": {
        "name": "T-Shirt3",
        "description": "A classic fit t-shirt with a ribbed neckline. Made of 100% cotton. Comes in sizes S-XXL.",
        "price": "$20.00",
        "image": "/Users/adamtaieb/Downloads/tshirt3.png",
        "recommended": ["T-Shirt1", "T-Shirt2", "T-Shirt4"]
    },
    "T-Shirt4": {
        "name": "T-Shirt4",
        "description": "A classic fit t-shirt with a ribbed neckline. Made of 100% cotton. Comes in sizes S-XXL.",
        "price": "$20.00",
        "image": "/Users/adamtaieb/Downloads/tshirt4.png",
        "recommended": ["T-Shirt1", "T-Shirt2", "T-Shirt3"]
    },
    "Trouser1": {
        "name": "Trouser1",
        "description": "A pair of comfortable trouser made of 100% denim. Comes in sizes 28-40",
        "price": "$35.00",
        "image": "/Users/adamtaieb/Downloads/trousers1.png",
        "recommended": ["Trouser2", "Trouser3", "Trouser4"]
    },
    "Trouser2": {
        "name": "Trouser2",
        "description": "A pair of comfortable trouser made of 100% denim. Comes in sizes 28-40",
        "price": "$35.00",
        "image": "/Users/adamtaieb/Downloads/trousers2.png",
        "recommended": ["Trouser1", "Trouser3", "Trouser4"]
    },
    "Trouser3": {
        "name": "Trouser3",
        "description": "A pair of comfortable trouser made of 100% denim. Comes in sizes 28-40",
        "price": "$35.00",
        "image": "/Users/adamtaieb/Downloads/trousers3.png",
        "recommended": ["Trouser2", "Trouser4", "Trouser1"]
    },
    "Trouser4": {
        "name": "Trouser4",
        "description": "A pair of comfortable trouser made of 100% denim. Comes in sizes 28-40",
        "price": "$35.00",
        "image": "/Users/adamtaieb/Downloads/trousers4.png",
        "recommended": ["Trouser1", "Trouser2", "Trouser3"]
    },
    "Pullover1": {
        "name": "Pullover1",
        "description": "A classic pullover with a modern twist. Made of a cotton and polyester blend. Comes in sizes XS-L.",
        "price": "$65.00",
        "image": "/Users/adamtaieb/Downloads/pullover1.png",
        "recommended": ["Pullover4", "Pullover2", "Pullover3"]
    },
    "Pullover2": {
        "name": "Pullover2",
        "description": "A classic pullover with a modern twist. Made of a cotton and polyester blend. Comes in sizes XS-L.",
        "price": "$65.00",
        "image": "/Users/adamtaieb/Downloads/pullover2.png",
        "recommended": ["Pullover1", "Pullover3", "Pullover4"]
    },
    "Pullover3": {
        "name": "Pullover3",
        "description": "A classic pullover with a modern twist. Made of a cotton and polyester blend. Comes in sizes XS-L.",
        "price": "$65.00",
        "image": "/Users/adamtaieb/Downloads/pullover3.png",
        "recommended": ["Pullover1", "Pullover2", "Pullover4"]
    },
    "Pullover4": {
        "name": "Pullover4",
        "description": "A classic pullover with a modern twist. Made of a cotton and polyester blend. Comes in sizes XS-L.",
        "price": "$65.00",
        "image": "/Users/adamtaieb/Downloads/pullover4.png",
        "recommended": ["Pullover1", "Pullover2", "Pullover3"]
    },
    "Dress1": {
        "name": "Dress1",
        "description": "A beautiful dress made of silk. Perfect for a night out. Comes in sizes XS-L.",
        "price": "$100.00",
        "image": "/Users/adamtaieb/Downloads/dress1.png",
        "recommended": ["Dress2", "Dress3", "Dress4"]
    },
    "Dress2": {
        "name": "Dress2",
        "description": "A beautiful dress made of silk. Perfect for a night out. Comes in sizes XS-L.",
        "price": "$100.00",
        "image": "/Users/adamtaieb/Downloads/dress2.png",
        "recommended": ["Dress1", "Dress3", "Dress4"]
    },
    "Dress3": {
        "name": "Dress3",
        "description": "A beautiful dress made of silk. Perfect for a night out. Comes in sizes XS-L.",
        "price": "$100.00",
        "image": "/Users/adamtaieb/Downloads/dress3.png",
        "recommended": ["Dress1", "Dress2", "Dress4"]
    },
    "Dress4": {
        "name": "Dress4",
        "description": "A beautiful dress made of silk. Perfect for a night out. Comes in sizes XS-L.",
        "price": "$100.00",
        "image": "/Users/adamtaieb/Downloads/dress4.png",
        "recommended": ["Dress1", "Dress2", "Dress3"]
    },
    "Coat1": {
        "name": "Coat1",
        "description": "Stay warm and stylish this winter with our cozy and fashionable coat. Comes in sizes S-XL.",
        "price": "$125.00",
        "image": "/Users/adamtaieb/Downloads/coat1.png",
        "recommended": ["Coat2", "Coat3", "Coat4"]
    },
    "Coat2": {
        "name": "Coat2",
        "description": "Stay warm and stylish this winter with our cozy and fashionable coat. Comes in sizes S-XL.",
        "price": "$125.00",
        "image": "/Users/adamtaieb/Downloads/coat2.png",
        "recommended": ["Coat1", "Coat3", "Coat4"]
    },
    "Coat3": {
        "name": "Coat3",
        "description": "Stay warm and stylish this winter with our cozy and fashionable coat. Comes in sizes S-XL.",
        "price": "$125.00",
        "image": "/Users/adamtaieb/Downloads/coat3.png",
        "recommended": ["Coat1", "Coat2", "Coat4"]
    },
    "Coat4": {
        "name": "Coat4",
        "description": "Stay warm and stylish this winter with our cozy and fashionable coat. Comes in sizes S-XL.",
        "price": "$125.00",
        "image": "/Users/adamtaieb/Downloads/coat4.png",
        "recommended": ["Coat1", "Coat2", "Coat3"]
    },
    "Sandal1": {
        "name": "Sandal1",
        "description": "Step into summer with our sleek and comfortable sandals.",
        "price": "$45.00",
        "image": "/Users/adamtaieb/Downloads/sandals1.png",
        "recommended": ["Sandal2", "Sandal3", "Sandal4"]
    },
    "Sandal2": {
        "name": "Sandal2",
        "description": "Step into summer with our sleek and comfortable sandals.",
        "price": "$45.00",
        "image": "/Users/adamtaieb/Downloads/sandals2.png",
        "recommended": ["Sandal1", "Sandal3", "Sandal4"]
    },
    "Sandal3": {
        "name": "Sandal3",
        "description": "Step into summer with our sleek and comfortable sandals.",
        "price": "$45.00",
        "image": "/Users/adamtaieb/Downloads/sandals3.png",
        "recommended": ["Sandal1", "Sandal2", "Sandal4"]
    },
    "Sandal4": {
        "name": "Sandal4",
        "description": "Step into summer with our sleek and comfortable sandals.",
        "price": "$45.00",
        "image": "/Users/adamtaieb/Downloads/sandals4.png",
        "recommended": ["Sandal1", "Sandal2", "Sandal3"]
    },
    "Shirt1": {
        "name": "Shirt1",
        "description": "Elevate your wardrobe with our versatile and comfortable shirt. Comes in sizes S-XL.",
        "price": "$60.00",
        "image": "/Users/adamtaieb/Downloads/shirt1.png",
        "recommended": ["Shirt2", "Shirt3", "Shirt4"]
    },
    "Shirt2": {
        "name": "Shirt2",
        "description": "Elevate your wardrobe with our versatile and comfortable shirt. Comes in sizes S-XL.",
        "price": "$60.00",
        "image": "/Users/adamtaieb/Downloads/shirt2.png",
        "recommended": ["Shirt1", "Shirt3", "Shirt4"]
    },
    "Shirt3": {
        "name": "Shirt3",
        "description": "Elevate your wardrobe with our versatile and comfortable shirt. Comes in sizes S-XL.",
        "price": "$60.00",
        "image": "/Users/adamtaieb/Downloads/shirt3.png",
        "recommended": ["Shirt1", "Shirt2", "Shirt4"]
    },
    "Shirt4": {
        "name": "Shirt4",
        "description": "Elevate your wardrobe with our versatile and comfortable shirt. Comes in sizes S-XL.",
        "price": "$60.00",
        "image": "/Users/adamtaieb/Downloads/shirt4.png",
        "recommended": ["Shirt1", "Shirt2", "Shirt3"]
    },
    "Sneaker1": {
        "name": "Sneaker1",
        "description": "Experience the perfect combination of style and comfort with our trendy and supportive sneaker.",
        "price": "$90.00",
        "image": "/Users/adamtaieb/Downloads/sneaker1.png",
        "recommended": ["Sneaker2", "Sneaker3", "Sneaker4"]
    },
    "Sneaker2": {
        "name": "Sneaker2",
        "description": "Experience the perfect combination of style and comfort with our trendy and supportive sneaker.",
        "price": "$90.00",
        "image": "/Users/adamtaieb/Downloads/sneaker2.png",
        "recommended": ["Sneaker1", "Sneaker3", "Sneaker4"]
    },
    "Sneaker3": {
        "name": "Sneaker3",
        "description": "Experience the perfect combination of style and comfort with our trendy and supportive sneaker.",
        "price": "$90.00",
        "image": "/Users/adamtaieb/Downloads/sneaker3.png",
        "recommended": ["Sneaker1", "Sneaker2", "Sneaker4"]
    },
    "Sneaker4": {
        "name": "Sneaker4",
        "description": "Experience the perfect combination of style and comfort with our trendy and supportive sneaker.",
        "price": "$90.00",
        "image": "/Users/adamtaieb/Downloads/sneaker4.png",
        "recommended": ["Sneaker1", "Sneaker2", "Sneaker3"]
    },
    "Bag1": {
        "name": "Bag1",
        "description": "Carry your essentials in style with our chic and functional bag.",
        "price": "$115.00",
        "image": "/Users/adamtaieb/Downloads/bag1.png",
        "recommended": ["Bag2", "Bag3", "Bag4"]
    },
    "Bag2": {
        "name": "Bag2",
        "description": "Carry your essentials in style with our chic and functional bag.",
        "price": "$115.00",
        "image": "/Users/adamtaieb/Downloads/bag2.png",
        "recommended": ["Bag1", "Bag3", "Bag4"]
    },
    "Bag3": {
        "name": "Bag3",
        "description": "Carry your essentials in style with our chic and functional bag.",
        "price": "$115.00",
        "image": "/Users/adamtaieb/Downloads/bag3.png",
        "recommended": ["Bag1", "Bag2", "Bag4"]
    },
    "Bag4": {
        "name": "Bag4",
        "description": "Carry your essentials in style with our chic and functional bag.",
        "price": "$115.00",
        "image": "/Users/adamtaieb/Downloads/bag4.png",
        "recommended": ["Bag1", "Bag2", "Bag3"]
    },
    "Boot1": {
        "name": "Boot1",
        "description": "Stay cozy and stylish this season with our fashionable and comfortable boots.",
        "price": "$150.00",
        "image": "/Users/adamtaieb/Downloads/boots1.png",
        "recommended": ["Boot2", "Boot3", "Boot4"]
    },
    "Boot2": {
        "name": "Boot2",
        "description": "Stay cozy and stylish this season with our fashionable and comfortable boots.",
        "price": "$150.00",
        "image": "/Users/adamtaieb/Downloads/boots2.png",
        "recommended": ["Boot1", "Boot3", "Boot4"]
    },
    "Boot3": {
        "name": "Boot3",
        "description": "Stay cozy and stylish this season with our fashionable and comfortable boots.",
        "price": "$150.00",
        "image": "/Users/adamtaieb/Downloads/boots3.png",
        "recommended": ["Boot1", "Boot2", "Boot4"]
    },
    "Boot4": {
        "name": "Boot4",
        "description": "Stay cozy and stylish this season with our fashionable and comfortable boots.",
        "price": "$150.00",
        "image": "/Users/adamtaieb/Downloads/boots4.png",
        "recommended": ["Boot1", "Boot2", "Boot3"]
    }
}

# Define a function to display a product
def display_product(product):
    st.write(f"## {product['name']}")
    st.write(product['description'])
    st.write(product['price'])
    st.image(product['image'])

# Define the main function
def main():
    st.set_page_config(page_title="Clothing Retailer", page_icon="🛍️", layout="wide")
    st.title("Shop")

    # Display the products in a grid of 3 by 3
    for i, (key, product) in enumerate(products.items()):
        if i % 3 == 0:
            col1, col2, col3 = st.columns(3)
        col = col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3
        col.write(f"### {product['name']}")
        col.image(product['image'])
        if col.button(f"View Item {i+1}"):
            st.write(f"You clicked on item {i+1}")
            display_product(product)
            st.write("## Recommended Products")
            for rec in product['recommended']:
                display_product(products[rec])

# Call the main function to run the app
main()
