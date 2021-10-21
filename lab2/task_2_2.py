import re


class TextFile:
    def __init__(self, myfile, characters=0, words=0, sentences=0):
        self.myfile = myfile
        self.characters = characters
        self._words = words
        self.sentences = sentences

    def numCharacters(self):
        try:
            with open('myfile.txt', 'r') as file:
                data = file.read()
                characters = data
        except FileNotFoundError:
            raise FileNotFoundError('Error.This file was not found')
        return f'Characters:{len(characters)}'

    def numWords(self):
        try:
            with open('myfile.txt', 'r') as file:
                data = file.read()
                words = data.split()
        except FileNotFoundError:
            raise FileNotFoundError('Error.This file was not found')
        return f'Words:{len(words)}'

    def numSentences(self):
        try:
            with open('myfile.txt', 'r') as file:
                data = file.read()
                file.seek(0)
                for line in file:
                    self.sentences += len(re.split('\. |! |\? |\[...]', line))
        except FileNotFoundError:
            raise FileNotFoundError('Error.This file was not found')
        return f'Sentences:{self.sentences}'


a = TextFile('myfile.txt')
print(a.numCharacters())
print(a.numWords())
print(a.numSentences())
