import sys
from stats import get_num_words
from stats import character_count    
from stats import sort_dic

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    char_counts = sort_dic(character_count(sys.argv[1]))
    for char_dict in char_counts:
        char = list(char_dict.keys())[0]
        count = list(char_dict.values())[0]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

    
main()