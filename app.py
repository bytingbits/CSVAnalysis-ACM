import streamlit as st

light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path
# Create columns for the header
col1, col2 = st.columns([1, 3])  # Adjust the ratios as needed

with col1:
    st.image(light_mode_logo, use_column_width=True)  # Display header image
# Set the title of the app
st.title("Welcome to ACM-CEG's Report Analyser!")
st.write("Hey! This tool helps you quickly pull insights from our feedback forms so that members of the HR domain can make expressive reports fast + events domain can get action points to be implemented in further events")

light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path
st.logo(light_mode_logo)
st.markdown("<div style='height: 10pc;'></div>", unsafe_allow_html=True)  # Adjust height as needed

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
    Made with ❤️ by <a href="https://github.com/bytingbits" target="_blank">Baby</a>
</div>
""", unsafe_allow_html=True)
