# Copied from http://t-redactyl.io/blog/2017/04/using-vader-to-handle-sentiment-analysis-with-social-media-text.html
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
print(analyser.polarity_scores("The food is good."))

# expect-output-to-have: {'neg': 0.0, 'neu': 0.508, 'pos': 0.492, 'compound': 0.4404}
