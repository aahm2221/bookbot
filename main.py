def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    word_count = word_counter(file_contents)
    char_count = char_counter(file_contents)
    char_info = sort_char(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.\n")
    for info in char_info:
        print(f"The '{info["name"]}' character was found {info["num"]} times.")
    print("--- End Report ---")

def sort_on(dict):
    return dict["num"]

def sort_char(char_dict):
    sorted = []
    for char in char_dict:
        sorted.append({"name": char, "num": char_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
    

def char_counter(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            if char.isalpha():
                chars[char.lower()] = 1
    return chars

def word_counter(text):
    return len(text.split())


def get_text(path):
    with open(path) as f:
       return f.read()

main()