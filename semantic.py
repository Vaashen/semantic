import spacy

# ----- Example 1 -----

nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# ---Notes on Example 1 ---
# cat and monkey are very similar because they are both animals
# monkey and banana are similar as well because monkeys really like bananas
# cats and banana are not very simlar because cats dont usually eat bananas


# ---- Example.py -----
# The simple language model displays information about what parts of speech each word in a sentence falls under.
# Where as the 'en_core_web_md' model compares two or more words, and finds out how similar they are from a scale of 0 to 1,
# 0 being the least similar and 1 being the most similar. It returns a decimal number for a more accurate reading.

 