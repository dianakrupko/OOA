import re


class TextFile:
    def __init__(self, myfile, characters=0, words=0, sentences=0):
        self.myfile = myfile
        self.characters = characters
        self.words = words
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
                for line in file:
                    for i in ['!', '?', '.',"'" ',','-', ':', ';']:
                        line = line.replace(i, ' ')
                    self.words += len(line.split())
        except FileNotFoundError:
            raise FileNotFoundError('Error.This file was not found')
        return f'Words:{self.words}'

    def numSentences(self):
        try:
            with open('myfile.txt', 'r') as file:
                file.seek(0)
                for line in file:
                    line=line.replace(' ', '')
                    for i in ['!', '?', '.']:
                        line = line.replace(i, ' ')
                    self.sentences += len(line.split())
        except FileNotFoundError:
            raise FileNotFoundError('Error.This file was not found')
        return f'Sentences:{self.sentences}'


a = TextFile('myfile.txt')
print(a.numCharacters())
print(a.numWords())
print(a.numSentences())