import re


class TextFile:
    def __init__(self, characters=0, words=0, sentences=0):
        self.characters = characters
        self._words = words
        self.sentences = sentences

    def numerate(self):
        try:
            with open('myfile.txt') as file:
                data = file.read()
                characters = data
                words = data.split()
                file.seek(0)
                for line in file:
                    self.sentences += len(re.split('\. |! |\? |\...', line))
        except FileNotFoundError:
            quit('Error.This file was not found')
        return f'Characters: {len(characters)} \nWords: {len(words)} \nSentences: {self.sentences}'


a = TextFile()
print(a.numerate())
