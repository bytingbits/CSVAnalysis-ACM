import streamlit as st
import pandas as pd

# Function to load CSV
def load_data(file):
    return pd.read_csv(file)

# Streamlit app layout
st.title("CSV Item Percentage Analysis")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load the data
    data = load_data(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data)

    # Detect object columns
    text_columns = data.select_dtypes(include=['object']).columns.tolist()
    selected_column = st.selectbox("Select a column for analysis:", text_columns)

    if selected_column:
        st.write(f"Selected Column: {selected_column}")
        
        # Calculate percentage of each unique item in the selected column
        percentage_counts = data[selected_column].value_counts(normalize=True) * 100
        percentage_counts = percentage_counts.reset_index()
        percentage_counts.columns = [selected_column, 'Percentage']
        
        # Display table with percentages
        st.write("Item Percentages:")
        st.dataframe(percentage_counts)

        # Display pie chart
        st.subheader("Pie Chart of Item Percentages")
        fig = percentage_counts.plot.pie(
        y='Percentage',
        labels=percentage_counts[selected_column],
        autopct='%1.1f%%',
        startangle=90,
        ylabel='',  # Remove y-label
        legend=None  # Do not show the legend
        ).figure
        st.pyplot(fig)
