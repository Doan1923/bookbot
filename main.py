import sys
print(sys.argv)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    text = get_book_text(path)
    wordCount = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    char_counts = get_char_count(text)
    print("--------- Character Count -------")
    sorted_chars = sort_char(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_word_count
from stats import get_char_count
from stats import sort_char


#runs the code?
if __name__ == "__main__":
    main()