# ProblemGenerator

Этот проект реализует генератор задач для линейного программирования, а также их решений симплекс методом

## Описание файлов

### main.py
Основной файл для исполнения. Генерирует заданной пользователем количество вариантов задач и решений к ним, после чего записывает эти данные в `.tex` файл

### generation.py
Реализует создание решаемой задачи: задает ограничения на переменные и создает целефую функцию

### solution.py
Реализует решение задачи оптимизации симплекс методом 

### latex_handler.py
Реализует функционал для записи задач и решений к ним в `.tex` файлы

### constants.py
Хранит в себе все константы, используемые в проекте, такие как численные ограничения на переменные задачи и названия выходных файлов по умолчанию