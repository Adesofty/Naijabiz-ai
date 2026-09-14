import streamlit as st
st.set_page_config(page_title="NaijaBiz AI", page_icon="🇳🇬")
st.title("🇳🇬 NaijaBiz AI")
st.caption("Pidgin + English Customer Assistant for Naija SMEs")
st.sidebar.header("My Business Setup")
biz = st.sidebar.text_input("Business Name","Softy Fashion Hub")
prod = st.sidebar.text_area("Products & Price","Men's Sneakers - 25k\nWomen Bags - 15k\nDelivery Ilorin, PH, Lagos 2k-4k")
loc = st.sidebar.text_input("Location","Ilorin & Port Harcourt")
q = st.text_input("Customer Message:","How much be that sneakers?")
if st.button("Reply Customer"):
    low = q.lower()
    if "how much" in low or "price" in low:
        st.success(f"{biz} price list:\n{prod}\nWhich one you like?")
    elif "deliver" in low:
        st.success(f"Yes! We deliver from {loc}. Delivery 2k-4k. Your location?")
    else:
        st.success(f"Thanks for contacting {biz}! We see: '{q}'. Drop WhatsApp.")
