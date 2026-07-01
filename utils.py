import streamlit as st

def svg(path, width=24):
    with open(path, "r", encoding="utf-8") as file:
        svg_code = file.read()

    st.image(svg_code, width=width)