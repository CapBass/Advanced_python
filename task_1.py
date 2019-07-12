import chardet


class Word:
    def __init__(self, name):
        self._name = name

    @property
    def word(self):
        return self._name

    def get_type(self):
        return type(self.word)

    def encode(self, encoding='utf-8'):
        self._name = self.word.encode(encoding)
        return self

    def decode(self):
        if isinstance(self.word, bytes):
            encoding = chardet.detect(self.word)['encoding']
            self._name = self.word.decode(encoding)
        return self


list_str = [Word('разработка'), Word('сокет'), Word('декоратор')]

for i, word in enumerate(list_str):
    print(f'{i + 1} слово {word.word} с типом {word.get_type()}')
    encoding = 'utf-8'
    word.encode(encoding)
    print(f'''в {encoding} имеет вид
           {word.word}
           и имеет тип {word.get_type()}''')
    word.decode()
    print(f'после обратого преобразования выглядит как \'{word.word}\' с типом {word.get_type()}')
