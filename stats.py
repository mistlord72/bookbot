def get_num_words(book):

    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
    return num_words 

def character_count(book):
    characters = {}
    
    with open(book) as f:
        words = f.read()
    if not words:
        return {}
    for char in words:
        tex = char.lower()
        if tex in characters:
            characters[tex] += 1 
        else:
            characters[tex] = 1

    return characters
def sort_on(dict_item):
    return list(dict_item.values())[0]

def sort_dic(dicts):
    counts = []
    for char, count in dicts.items():
        character_dic = {char: count}
        counts.append(character_dic)
        
    counts.sort(reverse=True, key=sort_on)

    return counts