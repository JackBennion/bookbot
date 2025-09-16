import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

input_file = sys.argv[1]

def get_book_text(book):
    file_contents = book.read()
    return file_contents

from stats import get_num_key, sort_dict, get_num_char, get_num_words

def main():
    with open(input_file) as f:
        text = get_book_text(f)
        word_count = get_num_words(text)
        num_char = get_num_char(text)
        sorted_list = sort_dict(num_char)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        for char_info in sorted_list:
            char = char_info["char"]
            count = char_info["num"]
            
            if char.isalpha():
                    print(f"{char}: {count}")

main()
