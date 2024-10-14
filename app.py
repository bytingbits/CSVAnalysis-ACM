import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from statistics import mode, mean, median

def load_data(file):
    return pd.read_csv(file)

def create_stacked_bar_plot(df, x_column, y_column):
    # Group the data by the two selected columns, counting occurrences
    grouped_data = df.groupby([x_column, y_column]).size().unstack(fill_value=0)
    
    # Create the stacked bar plot
    fig = go.Figure()
    
    for category in grouped_data.columns:
        fig.add_trace(go.Bar(
            x=grouped_data.index,
            y=grouped_data[category],
            name=str(category)
        ))
    
    fig.update_layout(
        barmode='stack',
        title=f'Distribution of {y_column} by {x_column}',
        xaxis_title=x_column,
        yaxis_title='Count',
        legend_title=y_column
    )
    
    return fig

def create_pivot_table(df, x_column, y_column):
    return pd.pivot_table(df, values=df.index, index=x_column, columns=y_column, aggfunc='count', fill_value=0)

def display_statistics(df, column):
    if pd.api.types.is_numeric_dtype(df[column]):
        col1, col2, col3 = st.columns(3)
        col1.metric("Mean", f"{mean(df[column]):.2f}")
        col2.metric("Median", f"{median(df[column]):.2f}")
        col3.metric("Mode", f"{mode(df[column]):.2f}")
    else:
        st.metric("Mode", mode(df[column]))

def main():
    st.title("CSV Data Visualizer")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        columns = df.columns.tolist()
        x_column = st.selectbox("Select column for X-axis", columns)
        y_column = st.selectbox("Select column for Y-axis (stacked)", columns)

        if x_column and y_column:
            fig = create_stacked_bar_plot(df, x_column, y_column)
            st.plotly_chart(fig)

            st.subheader("Pivot Table")
            pivot_table = create_pivot_table(df, x_column, y_column)
            st.dataframe(pivot_table)

            st.subheader(f"Statistics for {x_column}")
            display_statistics(df, x_column)

            st.subheader(f"Statistics for {y_column}")
            display_statistics(df, y_column)

if __name__ == "__main__":
    main()
