def is_pangram(sentence):
    lst = []
    sentence = (list(sentence.lower()))
    target = 26
    unwanted = [" ", ",", '', ' ', "_", "1", "2", "3", ".", "\""]
    for letter in sentence:
        if letter not in lst and letter not in unwanted:
            lst.append(letter)
    if len(set(lst)) == target:
        return True
    else:
        return False


