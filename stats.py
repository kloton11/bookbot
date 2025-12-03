def count_words_in_book(book_text):
    number_words = 0

    words = book_text.split()
    for word in words:
        number_words += 1

    return number_words


def count_characters(book_text):
    characters = {}

    for ch in book_text:
        ch = ch.lower()
        if ch in characters:
            characters[ch] += 1

        else:
            characters[ch] = 1

    return characters


def sort_on_num(item):
    return item["num"]

def sort_char_dict(character_dict):

    char_list = []

    for ch, count in character_dict.items():
        char_list.append({
            "char" : ch,
            "num" : count
        })

    char_list.sort(key=sort_on_num, reverse=True)

    return char_list

 
