import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load CSV
def load_data(file):
    return pd.read_csv(file)

# Function to aggregate small percentages
def aggregate_small_percentages(df, threshold):
    mask = df['Percentage'] < threshold
    if mask.any():
        # Sum up all percentages below threshold
        others_sum = df.loc[mask, 'Percentage'].sum()
        # Keep rows above threshold
        df_filtered = df[~mask].copy()
        # Add the "Others" row
        others_row = pd.DataFrame({
            df.columns[0]: ['Others'],
            'Percentage': [others_sum]
        })
        return pd.concat([df_filtered, others_row], ignore_index=True)
    return df

# Streamlit app layout
st.title("Pie Chart")

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
        
        # Add threshold slider
        threshold = st.slider(
            "Aggregate items below threshold (%)",
            min_value=0.0,
            max_value=50.0,
            value=0.0,
            step=0.1,
            help="Items with percentage below this threshold will be grouped as 'Others'"
        )
        
        # Calculate percentage of each unique item in the selected column
        percentage_counts = data[selected_column].value_counts(normalize=True) * 100
        percentage_counts = percentage_counts.reset_index()
        percentage_counts.columns = [selected_column, 'Percentage']
        
        # Apply threshold aggregation
        percentage_counts = aggregate_small_percentages(percentage_counts, threshold)
        
        # Display table with percentages
        st.write("Item Percentages:")
        st.dataframe(percentage_counts)
        
        # Display pie chart
        st.subheader("Pie Chart of Item Percentages")
        
        # Create figure and axis objects with a single subplot
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            percentage_counts['Percentage'],
            labels=percentage_counts[selected_column],
            autopct='%1.1f%%',
            startangle=90
        )
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        
        # Add some spacing between percentage labels and pie slices
        plt.setp(autotexts, size=8)
        plt.setp(texts, size=8)
        
        # Display the plot
        st.pyplot(fig)