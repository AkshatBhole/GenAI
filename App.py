import streamlit as st
import langchain
import langchain_helper

st.title("Restaurant Name and Menu Generator")

st.sidebar.header("User Input")
cuisine = st.sidebar.text_input("Enter the cuisine type:")

if cuisine:
    response=langchain_helper.generate_name_and_menu(cuisine)
    st.header(f" {response['restaurant_name']}")
    menu_items=response['menu_items'].split(",")
    st.write("Menu Items:")

    for item in menu_items:
        st.write(f"- {item}")






