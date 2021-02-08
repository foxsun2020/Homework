"""
Python Example
===============
Generating a wordcloud from the txt file using Python.
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the whole text from txt.
fp = r"C:\Users\fox\Documents\news.txt"
text = open(fp, encoding='utf-8').read()

# Generate a word cloud image
word_cloud = WordCloud(
    font_path=r'C:\Windows\Fonts\msyh.ttc',
    width=400,  # width of the canvas.
    height=200,  # height of the canvas.
    max_font_size=150,
    font_step=5,
    background_color="white",
    random_state=3,
    margin=3,
    colormap="tab20"  # matplotlib colormap
).generate(text)

# Display the generated image in matplotlib way:
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
