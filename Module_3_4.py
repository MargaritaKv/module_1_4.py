def single_root_words (root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.startswith (root_word):
            same_words.append (word)
    return same_words
result = single_root_words ('яблоко', 'яблочный', 'яблокова', 'цветочек', 'яблоки', 'гулять')
print (result)
