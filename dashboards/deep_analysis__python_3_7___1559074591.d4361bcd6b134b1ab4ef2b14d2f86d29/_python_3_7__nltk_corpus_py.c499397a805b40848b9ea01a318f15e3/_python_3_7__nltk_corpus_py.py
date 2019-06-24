# Copied from https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk

from nltk.corpus import twitter_samples
print(twitter_samples.fileids())

# expect-output-to-have: 'negative_tweets.json'
# expect-output-to-have: 'positive_tweets.json'
# expect-output-to-have: 'tweets.20150430-223406.json']
