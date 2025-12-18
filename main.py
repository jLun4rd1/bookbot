import sys
from stats import get_word_count, get_character_count, sort_dictionary


def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    contents = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    word_count = get_word_count(contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_count_dict = get_character_count(contents)
    sorted_list = sort_dictionary(character_count_dict)
    for dictionary in sorted_list:
        if not dictionary["char"].isalpha():
            continue
        print(f"{dictionary["char"]}: {dictionary["count"]}")

    print("============= END ===============")

main()