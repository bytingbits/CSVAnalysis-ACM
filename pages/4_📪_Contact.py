import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Don't be a stranger, get in touch!")

st.markdown("If you have better name ideas, questions or feature suggestions, mail me at <a href='mailto:csm.sharada@gmail.com'>csm.sharada@gmail.com</a> with the subject as 'ACM Reports Site'", unsafe_allow_html=True)

st.markdown("Don't like mails or prefer being anonymous? Fill this form instead! 🕵️", unsafe_allow_html=True)

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
    Powered by 🦄 and 🐿️
</div>
""", unsafe_allow_html=True)
