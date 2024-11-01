def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    word_count = word_counter(file_contents)
    print(word_count)

def word_counter(text):
    return len(text.split())


def get_text(path):
    with open(path) as f:
       return f.read()

main()