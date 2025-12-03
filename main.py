import sys
from stats import count_characters, count_words_in_book, sort_char_dict


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_path = sys.argv[1]
    
    
    book_text = get_book_text(book_path)
    
    
    num_words = count_words_in_book(book_text)
    print(f"Found {num_words} total words")
    
    
    character_counts = count_characters(book_text)
    sorted_chars = sort_char_dict(character_counts)

    
    print("============ BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("------- Character Count --------")
    
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

    print("========== END =========")

main()




