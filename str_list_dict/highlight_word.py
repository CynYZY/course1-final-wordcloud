def highlight_word(sentence, word):
    start = sentence.find(word)
    highlight = sentence[start : len(word)+start]
    return sentence[0 : start] + highlight.upper() + sentence[len(word)+start : ]
print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))