import os


def load_data(path_to_file):
    if not os.path.exists(path_to_file):
        return None
    with open(path_to_file, 'r') as words_file:
        file_dictionary = words_file.read().split(' ')
    return file_dictionary


def get_most_frequent_words(text):
    counts_word = {word: text.count(word) for word in text}
    return counts_word


if __name__ == '__main__':
    file_name = input('Введите путь к файлу ')
    data = load_data(file_name)
    if data is None:
        print('Хьюстон у нас проблемы, возможно не верно указан путь к файлу')
    else:
        load_dictionary = get_most_frequent_words()
        sort_dictionary = sorted(load_dictionary.items(), key = lambda l: l[1], reverse=True)
        for i in range(0,9):
            print (sort_dictionary[i][0],'-' ,sort_dictionary[i][1])
