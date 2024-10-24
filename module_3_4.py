def single_root_words(root_word, *other_words):
    same_words = []
    list_lower = [w.lower() for w in other_words]
    w_lower = root_word.lower()
    for i in list_lower:
        if w_lower in i or i in w_lower:
            same_words.append(i)
    return same_words



print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

