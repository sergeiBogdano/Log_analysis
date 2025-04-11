# Django Log Analyzer

Этот проект представляет собой CLI-приложение для анализа логов Django-приложений
и формирования отчетов о состоянии ручек API по каждому уровню логирования.

## Содержание
- [Описание](#описание)
- [Требования](#требования)
- [Структура проекта](#структура-проекта)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Ошибки](#ошибки)


## Описание
Программа анализирует логи Django-приложений,
позволяя пользователю передавать пути к файлам логов и запрашивать отчеты о ручках API.
Отчет формируется в виде таблицы и выводится в консоль.

## Требования
- Python 3.6 или выше
- Установленный `pytest` для тестирования


### Установка зависимостей
Для установки необходимых библиотек можно использовать файл `requirements.txt`:


### Структура проекта
```bash

pip install -r requirements.txt
Структура проекта
bash
Копировать
Редактировать
log_analyzer/
├── main.py               # Точка входа в приложение
├── log_parser.py         # Парсер логов
├── report_generator.py    # Генерация отчетов
├── reports/              # Модуль с отчетами
│   ├── __init__.py
│   └── handlers.py       # Логика генерации отчета для ручек API
├── utils.py              # Утилиты для форматирования вывода
├── requirements.txt      # Зависимости проекта
└── tests/                # Тесты
    └── test_generate_report.py  # Тесты для проверки функциональности отчета
```

### Использование
Для запуска приложения откройте терминал и выполните следующую команду:


 ```bash
Копировать
Редактировать
python main.py <path_to_log1> <path_to_log2> ... --report handlers
Пример:

bash
Копировать
Редактировать
python main.py logs/app1.log logs/app2.log logs/app3.log --report handlers
```
https://github.com/user-attachments/assets/663be30e-9b02-4002-bea7-ce69f9483d53

### Тестирование
Для запуска тестов используйте команду:

```bash
Копировать
Редактировать
pytest tests/
```
Примечание
В проекте присутствует один тест, который не проходит.
 Тест ожидает форматированного вывода,
  который отличается от реального из-за расхождений в ширине столбцов.
   Хотя логика формирования отчета правильная, необходимо скорректировать форматирование для соответствия требованиям теста.


### Ошибки
Если вы столкнетесь с ошибками или проблемами, пожалуйста, проверьте,
 что вы используете актуальные версии Python и необходимых библиотек.
  Для исправления ошибок вы также можете обратиться к документации Python или GitHub.
