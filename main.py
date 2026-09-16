# ./books/frankenstein.txt

def get_book_text(path_to_file): 
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def main(): 
    booktext = get_book_text("./books/frankenstein.txt")
    print(booktext)
main()
