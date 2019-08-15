import os
from xml.dom import minidom

class Xmlparser():

    def __init__(self, inputPath):
        self._inputPath = inputPath

    def parse(self, outputFilepath, inputPath):
        sentenceCounter = 0;
        globalResult = []

        for filename in os.listdir(inputPath):

            globalResult += self.parseSingle(inputPath + filename)

            file = open(outputFilepath, 'w', encoding='utf-8')

            for sentence in globalResult:
                sentenceCounter += 1;
                file.write(str(sentenceCounter) + " " + sentence)
                file.write('\n')

        file.close()

        return globalResult

    def parseSingle(self, filepath):
        Word = ""
        Disamb = ""
        Morph = ""
        IOBPrefix = ""
        IOB = ""
        Sentence = ""
        Sentences = []

        mydoc = minidom.parse(filepath)
        items = mydoc.getElementsByTagName('tok')

        for item in items:
            IOB = 'O'
            IOBPrefix = ""
            Word = item.childNodes[1].firstChild.data
            for childNode in item.childNodes:
                if childNode.attributes:
                    if 'disamb' in childNode.attributes:
                        Disamb = childNode.firstChild.firstChild.data
                        Morph = childNode.lastChild.lastChild.data
                    if 'chan' in childNode.attributes:
                        if childNode.firstChild.data != '0':
                            IOB = childNode.attributes._attrs['chan']._value
                    if 'key' in childNode.attributes:
                        IOBPrefix = 'B-'
                    else:
                        IOBPrefix = 'I-'

            if IOB != 'O':
                IOB = IOBPrefix + IOB

            Sentence = Word + " " + Disamb + " " + Morph + " " + IOB
            Sentences.append(Sentence)
        return Sentences

