from stats import count_words
from stats import count_characters
from stats import sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(relative_path):
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


main("books/frankenstein.txt")
