"""
Adapted from: https://github.com/amueller/word_cloud/blob/master/examples/simple.py
"""
from wordcloud import WordCloud

# Read the whole text.
text = 'We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility'

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

periscope.output(plt)

# expect-image
