def count_characters(book_text: str) -> dict[str, int]:
    char_counts = {}
    for char in book_text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char
