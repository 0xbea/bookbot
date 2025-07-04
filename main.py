from stats import count_words
from stats import count_characters
from stats import sort_chars
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    num_words = count_words(get_book_text(relative_path))
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_characters = sort_chars(count_characters(get_book_text(relative_path)))
    for dict in num_characters:
        # print(dict)
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    # print(num_characters)


main()
