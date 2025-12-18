def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    total_count_dict = {}
    for word in book_text.split():
        for character in word.lower():
            if character not in total_count_dict:
                total_count_dict[character] = 1
            else:
                total_count_dict[character] += 1
    return total_count_dict

def _sort_on(char_dict):
    return char_dict["count"]

def sort_dictionary(characters_dict):
    dict_list = []
    for key in characters_dict:
        dict_list.append(
            {
                "char": key,
                "count": characters_dict[key]
            }
        )
    dict_list.sort(reverse=True, key=_sort_on)
    return dict_list
