def is_pangram(sentence):
    sentence = sentence.lower()
    letters = [c for c in sentence if c.isalpha()]
    return len(set(letters)) == 26



