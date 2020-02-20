def pig_latin(text):
    # Separate the text into words
    words = text.split(" ")
    pl_list = []
    for word in words:
        # Create the pig latin word and add it to the list
        word =word[1:] + word[0] + "ay"
        pl_list.append(word)
    # Turn the list back into a phrase
    say = " ".join(pl_list)
    return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"