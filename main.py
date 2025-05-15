import sys
from stats import count_words, count_duplicate_words, sort_duplicated_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')
        print(f'Found {count_words(get_book_text(book_path))} total words')
        print('--------- Character Count -------')
        duplicate_words = count_duplicate_words(get_book_text(book_path))
        sorted_word_list = sort_duplicated_word_count(duplicate_words)
        for word, count in sorted_word_list.items():
            print(f'{word}: {count}')

main()
