import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk import ngrams
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import nltk

# Download necessary NLTK resources
nltk.download('vader_lexicon')

# Function to load CSV
def load_data(file):
    return pd.read_csv(file)

# N-gram analysis
def ngram_analysis(text_series, n=2):
    vectorizer = CountVectorizer(ngram_range=(n, n), stop_words='english')
    X = vectorizer.fit_transform(text_series)
    ngrams_counts = X.sum(axis=0).A1
    ngrams_list = vectorizer.get_feature_names_out()
    return pd.DataFrame({'N-gram': ngrams_list, 'Count': ngrams_counts}).sort_values(by='Count', ascending=False)

# Topic clustering (basic)
def topic_clustering(text_series, num_topics=5):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(text_series)
    topics = X.sum(axis=0).A1
    topics_df = pd.DataFrame({'Topic': vectorizer.get_feature_names_out(), 'Count': topics})
    return topics_df.sort_values(by='Count', ascending=False).head(num_topics)

# Sentiment analysis
def sentiment_analysis(text_series):
    sia = SentimentIntensityAnalyzer()
    sentiments = text_series.apply(lambda x: sia.polarity_scores(x))
    sentiments_df = pd.DataFrame(sentiments.tolist())
    sentiment_counts = sentiments_df['compound'].apply(lambda x: 'Positive' if x > 0.05 else ('Negative' if x < -0.05 else 'Neutral'))
    return sentiment_counts.value_counts()

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
        text_data = data[selected_column].dropna()

        # N-gram analysis
        st.subheader("N-gram Analysis")
        n = st.slider("Select N for N-grams:", 1, 5, 2)
        ngram_results = ngram_analysis(text_data, n)
        st.dataframe(ngram_results)
        if False: #commenting out code in progress
            # Topic clustering
            st.subheader("Topic Clustering")
            topic_results = topic_clustering(text_data)
            st.dataframe(topic_results)

            # Sentiment analysis
            st.subheader("Sentiment Analysis")
            sentiment_counts = sentiment_analysis(text_data)
            st.bar_chart(sentiment_counts)
 
            st.write("Sentiment Counts:")
            st.table(sentiment_counts)


