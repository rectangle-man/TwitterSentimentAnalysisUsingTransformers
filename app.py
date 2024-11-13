import tweepy
from preprocessor import Preprocess
from model import predict_sentiment
import streamlit as st


Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAO5vwwEAAAAAcwoJQ02Y9imUvEGtJNVByMviFro%3DegWEUT8fhtpt7pldMzhsT3KOFCZL9ylu3Za8uzoq52NenWRqlB"
client = tweepy.Client(bearer_token= Bearer_Token, wait_on_rate_limit=True)

input_query = ""

def fetch_tweet(query):
    tweets = client.search_recent_tweets(
        query=input_query, 
        tweet_fields=['context_annotations', 'created_at'], 
        max_results=10,
    )
    tweet_array = []

    tweets.data[0].text

    for i in range(len(tweets.data)):
        tweet_array.append(tweets.data[i].text)
    
    return tweet_array

def preprocess_tweets(tweet_array):
    preprocessor = Preprocess()

    processed_tweets = []
    for tweet in tweet_array:
      processed_tweets.append(preprocessor.preprocess_text(tweet))
    
    return processed_tweets

st.header("TWITTER SENTIMENT ANALYSTS :3")
st.write("This model will predict the sentiments of the topmost tweets fetched by your query.")

query = st.text_input(label="Enter your query to proceed")
if st.button("Submit"):
    tweet_array = fetch_tweet(query=query)
    preprocessed_tweets = preprocess_tweets(tweet_array=tweet_array)
    for i in range(len(preprocessed_tweets)):
        st.header("Tweet:")
        st.write(preprocessed_tweets[i])
        st.header("Sentiment")
        st.write(predict_sentiment(tweet=preprocessed_tweets[i]))