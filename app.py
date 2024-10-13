%%writefile app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot the unsorted stacked bar graph
def plot_unsorted_stacked_bar(df, column_a, column_b):
    # Create a pivot table to count the occurrences for stacking
    pivot_df = df.pivot_table(index=column_a, columns=column_b, aggfunc='size', fill_value=0)

    # Plot the unsorted stacked bar plot
    pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(f"Unsorted Stacked Bar Chart of {column_a} by {column_b}")
    plt.ylabel("Frequency")
    plt.xlabel(column_a)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt.gcf())  # Streamlit method to show the plot

# Function to plot the sorted stacked bar graph
def plot_sorted_stacked_bar(df, column_a, column_b):
    # Create a pivot table to count the occurrences for stacking
    pivot_df = df.pivot_table(index=column_a, columns=column_b, aggfunc='size', fill_value=0)

    # Sort the pivot table based on total frequency (sum across rows)
    pivot_df = pivot_df.loc[pivot_df.sum(axis=1).sort_values(ascending=False).index]

    # Plot the sorted stacked bar plot
    pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(f"Sorted Stacked Bar Chart of {column_a} by {column_b}")
    plt.ylabel("Frequency")
    plt.xlabel(column_a)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt.gcf())  # Streamlit method to show the plot

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
        st.subheader("Unsorted Stacked Bar Plot")
        plot_unsorted_stacked_bar(df, column_a, column_b)

        st.subheader("Sorted Stacked Bar Plot")
        plot_sorted_stacked_bar(df, column_a, column_b)

