gitimport streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot stacked sorted bar graph and show the pivot table
def plot_stacked_bar(df, column_a, column_b):
    # Create a pivot table to count occurrences for stacking
    pivot_df = df.pivot_table(index=column_a, columns=column_b, aggfunc='size', fill_value=0)

    # Sort the pivot table based on total frequency (sum across rows)
    pivot_df = pivot_df.loc[pivot_df.sum(axis=1).sort_values(ascending=False).index]

    # Display the pivot table in Streamlit
    st.write("Frequency Table:", pivot_df)

    # Plot the stacked bar chart
    pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(f"Stacked Bar Chart of {column_a} by {column_b}")
    plt.ylabel("Frequency")
    plt.xlabel(column_a)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt.gcf())  # Display plot in Streamlit

# Streamlit app layout
st.title("Stacked Bar Plot from CSV")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    # Step 2: Load CSV data
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Step 3: Dropdown for column selection
    columns = df.columns.tolist()
    column_a = st.selectbox("Select the column for X-axis (Column A):", columns)
    column_b = st.selectbox("Select the column for stacking (Column B):", columns)

    if st.button("Generate Plot"):
        plot_stacked_bar(df, column_a, column_b)
