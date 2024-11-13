from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax


def predict_sentiment(tweet):

      
    roberta = "cardiffnlp/twitter-roberta-base-sentiment"

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']
    # encoded_tweets = []
    # for tweet in processed_tweets:
    encoded_tweet = tokenizer(tweet, return_tensors='pt')


    output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    # outputs.append(scores)

    sentiment = labels[scores.argmax()]

    return sentiment