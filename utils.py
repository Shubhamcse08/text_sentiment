from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon (only first time)
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze sentiment using NLTK's VADER.
    Returns a dictionary with sentiment scores and label.
    """
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    scores['sentiment'] = sentiment
    return scores
