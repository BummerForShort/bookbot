import sys

from stats import get_num_words

from stats import numbers_of_letters

filepath = sys.argv

def main(filepath):
    if len(filepath) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(get_num_words(filepath[1]))
    print("--------- Character Count -------")
    sorted_count = numbers_of_letters(filepath[1])
    for letter in sorted_count:
        number = sorted_count[letter]
        print(f"{letter}: {number}")

main(filepath)