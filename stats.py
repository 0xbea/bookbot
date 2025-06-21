def count_words(text):
    return len(text.split())


# takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
def count_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(items):
    return items["num"]


# takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
def sort_chars(dict):
    char_count_list = []
    for char in dict:
        char_count_list.append({"char": char, "num": dict[char]})
    char_count_list.sort(reverse=True, key=sort_on)
    # print(char_count_list)
    return char_count_list
