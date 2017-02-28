import os
import re
import collections
import argparse


def load_data(path_to_file):
    if not os.path.exists(path_to_file):
        return None
    with open(path_to_file, 'r') as words_file:
        text = words_file.read()
    return text


def get_most_frequent_words(text):
    counts_word = re.sub("[^\w]", " ", text).split()
    return counts_word


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-load","-l", type=str, help="Указываем имя файла для обработки")
    namespace = parser.parse_args()
    if namespace.load:
        data_input = load_data(namespace.load)
        load_data_list = get_most_frequent_words(data_input)
        words_and_counts = collections.Counter(load_data_list).most_common(10)
        for word, count in words_and_counts:
            print('Слово "{0}" встречалось в тексте {1} раз(а) '.format(word, count))
    else:
        file_name = input('Введите путь к файлу ')
        data_input = load_data(file_name)
        if data_input is None:
            print('Хьюстон у нас проблемы, возможно не верно указан путь к файлу')
        else:
            load_data_list = get_most_frequent_words(data_input)
            words_and_counts = collections.Counter(load_data_list).most_common(10)
            for word, count in words_and_counts:
                print('Слово "{0}" встречалось в тексте {1} раз(а) '.format(word, count))
