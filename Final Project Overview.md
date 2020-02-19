# Final Project Overview

## Word Cloud

### Goal

Create a dictionary with ==words and word frequencies== that can be passed to the `generate_from_frequencies` function of the WordCloud class.

```python
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
# Once having the dictionary, use this code to generate the word cloud image
```

- external Python module

> creatively Word cloud

- create a script that would go through the text and count how many times each word appears

> Dictionary

#### Attention

- punctuation marks 	`isalpha()`
- split text in to words   `split()`
- find a way to exclude irrelevant or uninteresting words when processing the text
- only text file