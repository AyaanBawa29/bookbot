def count_words(book_text: str) -> int:
    return len(book_text.split())

def count_characters(book_text: str) -> dict[str, int]:
    char_counts = {}
    for char in book_text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(item: tuple[str, int]) -> int: 
    return item[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]: 
    my_list = []
    for char in chars_dict.keys():
        count = chars_dict[char]
        my_list.append((char, count))
    return sorted(my_list, key=sort_on, reverse=True)

def list_function(): 
    my_list = []
    my_list.append("item")
    return my_list 

