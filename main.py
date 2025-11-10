
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text, get_chars_dic, get_num_words, get_sorted_chars_list

def main():
    path_to_book = sys.argv[1]
    books_content = get_book_text(path_to_book)
    num_words = get_num_words(books_content)
    chars_dic = get_chars_dic(books_content)
    sorted_chars_list = get_sorted_chars_list(chars_dic)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dic in sorted_chars_list:
        char = char_dic["char"]
        if char.isalpha():
            print(f"{char}: {char_dic["num"]}")
    print("============= END ===============")


main()