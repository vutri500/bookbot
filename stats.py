def count_words(text):
    words = text.split()
    return len(words)

def count_duplicate_words(text):
    duplicate = {}
    words = text.split()
    for word in words:
        for character in word:
            character = character.lower()
            if character in duplicate:
                duplicate[character] += 1
            else:
                duplicate[character] = 1
    return duplicate

def sort_duplicated_word_count(word_list):
    words = list(word_list.keys())
    words.sort()

    sorted_word_list = {}
    for word in words:
        if word.isalpha():
            sorted_word_list[word] = word_list[word]

    return sorted_word_list