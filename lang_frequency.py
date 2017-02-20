import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as words_file:
        file_dictionary = words_file.read().split(' ')
    return file_dictionary


def get_most_frequent_words(text):
    letter_counts = {letter: text.count(letter) for letter in text}
    return letter_counts


if __name__ == '__main__':
    file_name = input('Введите путь к файлу ')
    data = load_data(file_name)
    if data is None:
        print('Хьюстон у нас проблемы, возможно не верно указан путь к файлу')
    else:
        load_dictionary = get_most_frequent_words()
        list_sorted = sorted(load_dictionary.items(), key = lambda l: l[1], reverse=True)
        for i in range(0,9):
            print (list_sorted[i][0],'-' ,list_sorted[i][1])
