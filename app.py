import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title="My App Title", page_icon="🌟")

light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path
# Create columns for the header
col1, col2 = st.columns([1, 5])  # Adjust the ratios as needed

with col1:
    st.image(light_mode_logo, use_column_width=True)  # Display header image
# Set the title of the app
with col2:
    st.title("Welcome to ACM-CEG's Report Analyser!")
st.write("Hey! 👋 This site is to help you make sense of our (often overwhelmingly large) Google Forms for reports and otherwise!") 
st.write("📊 You'll need a CSV file to use this site!") 
st.write("🧑‍💻 Once you've converted your files, navigate through the sidebar to upload it and create charts and tables! Have fun 🎉")

st.markdown('<a href="https://scribehow.com/shared/How_to_convert_a_Google_Sheet_to_a_CSV__z_ytbPzaRqysSF_FwqGt8g" target="_blank">Learn to convert a Google Sheet to a CSV, use this!</a>', unsafe_allow_html=True)

light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path
st.logo(light_mode_logo)
st.markdown("""
<style>

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(255, 255, 255, 0.8);
    color: black;
    text-align: center;
    padding: 10px;
    border-top: 1px solid #ccc;
    z-index: 1000;
}
</style>

<div class="footer">
    Made with 🍩 and 🍿
</div>
""", unsafe_allow_html=True)
