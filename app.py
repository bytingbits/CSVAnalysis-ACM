import streamlit as st

# Set the title of the app
st.title("Welcome to ACM-CEG's Report Analyser!")
st.write("Hey! This tool helps you quickly pull insights from our feedback forms so that members of the HR domain can make expressive reports fast + events domain can get action points to be implemented in further events")

# Define paths to your images
dark_mode_logo = "black_mode.png"  # Replace with your dark mode logo path
light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path

# Create a radio button to switch between light and dark modes
mode = st.radio("Choose mode:", options=["☀️ Light", "🌙 Dark"])

# Store the selected theme in session state
if 'theme' not in st.session_state:
    st.session_state.theme = "light"  # Default to light mode

if mode == "☀️ Light":
    st.session_state.theme = "light"
    st.image(light_mode_logo, caption="Light Mode Logo")
else:
    st.session_state.theme = "dark"
    st.image(dark_mode_logo, caption="Dark Mode Logo")

# Apply theme based on session state
if st.session_state.theme == "dark":
    st.markdown('<style>body {background-color: #000000; color: #ffffff;}</style>', unsafe_allow_html=True)
else:
    st.markdown('<style>body {background-color: #ffffff; color: #000000;}</style>', unsafe_allow_html=True)

st.write("Toggle between light and dark mode to see different logos.")
