import streamlit as st

def main():
    st.title("Terms and Policies")

    st.header("Terms of Service")
    st.write("By using our website, you agree to comply with our terms of service. These terms govern your use of the website and all services provided through the website.")

    st.subheader("Purchases")
    st.write("All purchases made through our website are final. We do not offer refunds or exchanges unless the item is defective or damaged upon arrival.")

    st.write("If you receive a defective or damaged item, please contact us within 14 days of receiving your order to arrange for a return or exchange. We may require photo evidence of the defect or damage before approving a return or exchange.")

    st.write("Please note that we cannot guarantee the availability of any item listed on our website. In the event that an item is out of stock, we will notify you as soon as possible and offer a full refund or suggest a similar alternative.")

    st.subheader("Privacy")
    st.write("We take your privacy seriously and will only use your personal information to fulfill your order and to communicate with you about your order. We will never sell your information to third parties.")

    st.write("By using our website, you consent to the collection and use of your personal information in accordance with our privacy policy. If you have any questions or concerns about our privacy policy, please contact us.")

    st.header("Shipping and Delivery")
    st.write("We offer free standard shipping on all orders over $50. Orders are processed and shipped within 1-2 business days. Delivery times may vary depending on your location and shipping method.")

    st.write("Please note that we are not responsible for any customs or import duties that may be charged upon delivery to international customers. We advise you to check with your local customs office for more information.")

    st.write("If you require express shipping, please contact us before placing your order to arrange for expedited shipping. Additional fees may apply.")

    st.header("Returns and Exchanges")
    st.write("If you receive a defective or damaged item, please contact us within 14 days of receiving your order to arrange for a return or exchange. We do not accept returns or exchanges for items that have been worn or washed.")

    st.write("To initiate a return or exchange, please contact us with your order number and a description of the issue. We may require photo evidence of the defect or damage before approving a return or exchange.")

    st.write("Please note that the customer is responsible for all return shipping costs, unless the item was defective or damaged upon arrival. Refunds will be issued to the original payment method within 3-5 business days of receiving the returned item.")

if __name__ == '__main__':
    main()
