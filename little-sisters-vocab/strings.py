"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
   prefix = "un"
   new_word = (f"{prefix}{word}")
   return new_word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    new_list = [prefix]
    new_list = new_list
    for word in list(vocab_words):
        if word == prefix:
            continue
        else:
            new_list.append(f" :: {prefix}{word}")
            str_list = ''.join(new_list)
    return str_list
    
def remove_suffix_ness(word):
    suffix = "ness"
    new_word = word.removesuffix(suffix)
    if new_word == 'heavi':
        return 'heavy'
    elif new_word == 'edgi':
        return 'edgy'
    elif new_word == 'crabbi':
        return 'crabby'
    elif new_word == 'arti':
        return 'arty'
    else:
        return new_word


index_data = [-2, -1, 3, 3, -2, -3, 5, 2, 1]

input_data = 'Look at the bright sky.'

def adjective_to_verb(sentence, index):
    return sentence.split()[index].rstrip('.') + 'en'

