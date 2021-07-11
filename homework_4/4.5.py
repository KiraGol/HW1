"""Splitting on sentences it is complicated task. You should use grouping but only for check. Before grouping should be placed your search query."""
import re

text = """Многие думают, что Lorem Ipsum - взятый с потолка псевдо-латинский набор слов, но это не совсем так.
Его корни уходят в один фрагмент классической латыни 45 года н.э., то есть более двух тысячелетий назад.
Ричард МакКлинток, профессор латыни из колледжа Hampden-Sydney, штат Вирджиния, взял одно из самых странных слов в Lorem Ipsum, "consectetur", и занялся его поисками в классической латинской литературе. В результате он нашёл неоспоримый первоисточник Lorem Ipsum в разделах 1.10.32 и 1.10.33 книги "de Finibus Bonorum et Malorum" ("О пределах добра и зла"), написанной Цицероном в 45 году н.э. Этот трактат по теории этики был очень популярен в эпоху Возрождения.
Первая строка Lorem Ipsum, "Lorem ipsum dolor sit amet..", происходит от одной из строк в разделе 1.10.32!"""

# (?=\s|$) - this means that right after your text which you are trying to
# find placed end of string or new line '\n'
# place search query insread of {}. You can say that each of your sentence
# start from [А-Я] then you can say that it could be any character . more
# from 1 to unlimited numbers of count. It could be or not be so I suggest
# to look on ? and each your sentence should be end with some kind
# of sybol [.!?]
sentences = re.findall(r"{}(?=\s|$)", text)
for sentence in sentences:
    print(f"\"{sentence}\"")