from stats import get_num_words
from stats import get_book_text
from stats import get_num_caracters
from stats import get_sort_letter_counts
import sys

def main():
    #path_to_file = 'books/frankenstein.txt'
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
        
    path_to_file = sys.argv[1] 
      
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    num_characters = get_num_caracters(book_text)
    sorted_letter_counts = get_sort_letter_counts(num_characters)
    #print(f'{num_characters} characters found in the document')    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for letter, count in sorted_letter_counts:
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")       
    
main()
