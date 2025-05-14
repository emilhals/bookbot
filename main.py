import sys
from stats import get_sorted_list_by_char, get_character_count, get_number_of_words

def main():
    print("============ BOOKBOT ============")

    print_report()

    print(str(sys.argv))


def print_report():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])
    
    word_count = get_number_of_words(text) 
    char_count = get_character_count(text)
    
    sorted_list = get_sorted_list_by_char(char_count)
    

    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")

    print("============= END ===============")



def get_book_text(filepath):
    file_contents = None

    try:
        with open(filepath) as f:
            file_contents = f.read()
    except Exception as e:
        return e

    return file_contents

main()
