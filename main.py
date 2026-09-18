# ./books/frankenstein.txt
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def print_report(block_path: str, word_count: int, sorted_chars_list: list[tuple[str, int]]):
    print(f"--- begin report of {block_path} ---")
    print(f"(word_count) words found in the document/n")
    for char, count in sorted_chars_list: 
        if char.isalpha():
            print(f"the '{char}' character was found {count} times")
    print("--- END ---")      

def main():
    booktext = get_book_text("./books/frankenstein.txt")
    char_counts_dict = count_characters(booktext)
    sorted_chars_list = chars_dict_to_sorted_list(char_counts_dict)
    print_report("./books/frankenstein.txt", count_words(booktext), sorted_chars_list)

main()


