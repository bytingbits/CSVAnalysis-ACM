# Sentiment analysis
def sentiment_analysis(text_series):
    sia = SentimentIntensityAnalyzer()
    sentiments = text_series.apply(lambda x: sia.polarity_scores(x))
    sentiments_df = pd.DataFrame(sentiments.tolist())
    sentiment_labels = sentiments_df['compound'].apply(lambda x: 'Positive' if x > 0.05 else ('Negative' if x < -0.05 else 'Neutral'))
    return pd.DataFrame({'Text': text_series, 'Sentiment': sentiment_labels})

# Streamlit app layout
st.title("Text Analysis")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(data)

    # Detect text columns
    text_columns = data.select_dtypes(include=['object']).columns.tolist()
    selected_column = st.selectbox("Select a text column for analysis:", text_columns)

    if selected_column:
        st.write(f"Selected Column: {selected_column}")
        text_data = data[selected_column].dropna()  # Drop null values

        # N-gram analysis
        st.subheader("N-gram Analysis")
        n = st.slider("Select N for N-grams:", 1, 5, 2)
        ngram_results = ngram_analysis(text_data, n)
        st.dataframe(ngram_results)

        # Sentiment analysis
        st.subheader("Sentiment Analysis")
        sentiment_results = sentiment_analysis(text_data)
        st.dataframe(sentiment_results)
