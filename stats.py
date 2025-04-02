def parse_book_text(string):
    list_of_words = string.split()
    return len(list_of_words)

def count_characters(string):
    dict_of_characters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    for character in string.lower():
        if (character not in dict_of_characters):
            dict_of_characters[character] = 0
        else:
            dict_of_characters[character] += 1
    
    return dict_of_characters

def sort_on(dict):
    return dict['amount']

def parse_dict(dict):
    new_list = []
    for character, value in dict.items():
        new_list.append({"character": character, "amount": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list
