# settings_parser

Постановка задачи

Кандидат должен реализовать парсер и сериализатор текстового
формата конфигурационного файла описанного ниже в виде модуля
python. Интерфейс модуля должен предоставлять возможность считать
конфигурационный файл, предоставить возможность работать
со значениями конфигурационного файла в удобном виде (в т.ч.
изменять, добавлять и удалять значения), а также сохранять измененные
значения обратно в конфигурационный файл. Организация интерфейса
модуля на усмотрение кандидата.


Не требуется анализировать и конвертировать типы данных значений,
значения должны быть предоставлены клиентскому коду в виде строк
или наборов строк.


Сериализатор должен максимально точно сохранять структуру исходного
файла, при внесении изменений, в том числе сохранять комментарии,
пустые строки, расположение директив относительно друг друга.


Описание формата

Конфигурационный файл является текстовым файлом в кодировке UTF-8.

Конфигурационные данные записаны построчно в формате:

<директива> <значение>

Директивы могут состоять из маленьких и больших букв латинского
алфавита, цифр, а также символов подчеркивания (_) и дефис (-) и
начинаться только с буквы латинского алфавита в любом регистре.

Значения являются произвольными UTF-8 строками, в том числе могут
быть пустой строкой. Какое-либо экранирование символов и значение
разбитые на несколько строк не поддерживаются.

И директивы и значения могут быть обрамлены с обоих сторон
произвольным количеством пробелов и/или табуляций, которые
не являются значимыми.

Строки с директивами могут быть разделены произвольным количеством
пустых строк, либо строк полностью состоящих из пробелов и/или табуляций.

В случае повторного использование одной и той же директивы в одном
файле учитывается только последнее значение.

Символом решетки (#) обозначает начало комментария, если:
    - он является первым символом строке за исключением пробелом и/или
      табуляций.
    - он следует за знащачим текстом строки и отделен от него как минимум
      одним пробелом или табуляцией.


Пример конфигурационного файла
# comment describing key1
key1 i'm a value of key1

# сomment
# describing
# key2

key2 value followed by comment    # commented text

key3 value with hash# sign        # actual comment

key3 repeated value of key 3      # consider only last one

key_with-long-strange_name        # and empty value


Используемые инструменты

Реализация должна работать с интерпретатором Python версии 2.7,
совместимость с версией 2.6 из поставки RHEL6 будет плюсом. Можно
использовать любые модули из состава стандартной библиотеки. При
использовании Python версии 2.6 допускается использовать модули
бэкпортированные из версии 2.7 и доступные в дистрибутиве RHEL6.

В отчете к выполнению тестового задания можно указать, какие
библиотеки для питона могли бы облегчить/упростить реализацию
задания, если таковые хотелось использовать. Исключение составляют
библиотеки реализующие аналогичный парсер/сериализатор.
