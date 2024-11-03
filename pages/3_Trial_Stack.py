import streamlit as st
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

# Function to plot bar chart of averages for numeric columns
def plot_average_bar(df, numeric_column, group_column):
    # Calculate the mean of numeric_column grouped by group_column
    avg_df = df.groupby(group_column)[numeric_column].mean().sort_values(ascending=False)
    st.write(type(avg_df)) #remove
    # Display the averages in Streamlit
    st.write("Average Table:", avg_df)

    # Plot the bar chart
    x=avg_df.iloc[:,0]
    y=avg_df.iloc[:,1]
    plt.figure(figsize=(10, 6))
    plt.bar(x,y)
    plt.title(f"Average of {numeric_column} grouped by {group_column}")
    plt.ylabel("Average")
    plt.xlabel(group_column)
    #plt.xticks(rotation=45, ha='right') #uncomment me
    plt.legend().set_visible(False)
    st.pyplot(plt.gcf())  # Display plot in Streamlit

# Streamlit app layout
st.title("Data Visualization from CSV")

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

    # Step 4: Option to select numeric column for averaging
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    selected_numeric_column = st.selectbox("Select a numeric column for averaging (Optional):", ["None"] + numeric_columns)
    group_column = st.selectbox("Select the column for grouping (if numeric column selected):", columns)

    if st.button("Generate Plot"):
        plot_stacked_bar(df, column_a, column_b)  # Generate the stacked bar plot

        # Generate average plot if numeric column is selected
        if selected_numeric_column != "None":
            plot_average_bar(df, selected_numeric_column, group_column)
