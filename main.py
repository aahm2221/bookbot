def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    word_count = word_counter(file_contents)
    print(word_count)
    char_count = char_counter(file_contents)
    for char in char_count:
        print(f"{char}: {char_count[char]}")

def char_counter(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            if char != "\n":
                chars[char.lower()] = 1
    return chars

def word_counter(text):
    return len(text.split())


def get_text(path):
    with open(path) as f:
       return f.read()

main()