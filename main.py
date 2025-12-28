import sys
from stats import word_count, character_count, character_count_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    count = word_count(text)
    chars = character_count(text)
    sorted_chars = character_count_sorted(chars)
    print_report(book_path, count, sorted_chars)

def print_report(book_path, count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
