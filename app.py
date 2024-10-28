import streamlit as st

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
    Made with ❤️ by <a href="https://github.com/your-github-username" target="_blank">Your Name</a>
</div>
""", unsafe_allow_html=True)
