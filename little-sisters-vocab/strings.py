"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
   prefix = "un"
   new_word = (f"{prefix}{word}")
   return new_word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    new_list = [] 
    for word in list(vocab_words):
        if word == prefix:
            continue
        else:
            new_list.append([f"{prefix}{word}"])
    return new_list
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    pass

print(make_word_groups(['en', 'circle', 'fold', 'close', 'joy', 'lighten', 'tangle', 'able', 'code', 'culture'])) 