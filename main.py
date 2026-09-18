import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def print_report(block_path: str, word_count: int, sorted_chars_list: list[tuple[str, int]]):
    print(f"--- begin report of {block_path} ---")
    print(f"(word_count) words found in the document\n")
    for char, count in sorted_chars_list: 
        if char.isalpha():
            print(f"the '{char}' character was found {count} times")
    print("--- END ---")      

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]


    booktext = get_book_text(book_path)
    char_counts_dict = count_characters(booktext)
    sorted_chars_list = chars_dict_to_sorted_list(char_counts_dict)
    print_report(book_path, count_words(booktext), sorted_chars_list)

main()

