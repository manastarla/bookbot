def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text
def get_num_words(book_text):
    words = book_text.split()
    return len(words)   

def get_num_caracters(book_text):
    letter_counts = {}
    for char in book_text.lower():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts

def get_sort_letter_counts(letter_counts):
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_letter_counts


  