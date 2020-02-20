from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open(r"C:\Users\Cynth\Documents\Google IT Automation with Python\Crash Course on Python\Final Project\Demo.txt", encoding="utf-8") as f:
    content = f.read()
    text = content.split(" ")
# Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
new_text = []
for w in text:
    if w not in punctuations:
        if w not in uninteresting_words:
            new_text.append(w)
counter = Counter(new_text)

cloud = WordCloud(background_color="white", width=800, height=600)
cloud.generate_from_frequencies(dict(counter.most_common(50)))
plt.imshow(cloud, interpolation="nearest")
plt.axis("off")
plt.show()
cloud.to_file('test.png')
