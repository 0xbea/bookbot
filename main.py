from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main(relative_path):
    num_words = count_words(get_book_text(relative_path))
    print(f"{num_words} words found in the document")


main("books/frankenstein.txt")
