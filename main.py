import sys
from stats import get_num_words, count_characters, sort_characters


def get_book_text(file_path):
    with open (file_path) as r:
        return r.read()
    

def main():
    
    book_path = ""

    if (len(sys.argv) < 2):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    
    file_text = get_book_text(book_path)

    num_words = get_num_words(file_text)
    
    char_count = count_characters(file_text)
    sorted_dict = sort_characters(char_count)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
