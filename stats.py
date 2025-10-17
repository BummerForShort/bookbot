def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    words = file_contents.split()
    num_words = len(words)
    return (f"Found {num_words} total words")

def numbers_of_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    lowercase_contents = file_contents.lower()
    letter_count = {}
    for l in lowercase_contents:
        if l not in letter_count:
            letter_count[l] = 1
        else:
            letter_count[l] += 1
    sorted_count = dict(sorted(letter_count.items(),key=lambda item: item[1], reverse=True))
    return sorted_count