# 5_lang_frequency

А вы знаете самые частые слова в русском языке? Это "и", "в" и "не". Остальных можно посмотреть на википедии.

В этой задаче нужно написать скрипт, который составит такой список для любого текста, поданного на вход.

Скрипт должен принимать на вход путь до текстового файла и выводить в консоль десять самых популярных слов в этом файле в порядке убывания частоты.

Потом можно попробовать скормить ему разные тексты. "Война и мир". Всю Википедию. Кстати, такой скрипт должен нормально работать не только с русским, но и с другими языками.

Запуск осуществляется двумя разными способами:
  1. стандартный - без указания параметров например python lang_frequency.py
  2. c параметрами - параметры запуска можно узнать с помощью python lang_frequency.py -h
  3. если требуется указать кодировку то запуск будет осуществляться так python find_repeat.py -load(-l) "имя файла" -encode(-en) "кодировка"

В результате запуска скрипт обрабатывает входной файл и осуществляет поиск самых частых слов в тексте.

Результатом работы скрипта является список из 10 самых популярных слов в файле в следующем формате:

* Слово "тут указывается слово" встречалось в тексте "количество сколько раз встречается слово" раз(а);

Например: Слово "и" встречалось в тексте 35 раз(а)
