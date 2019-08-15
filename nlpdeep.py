from xmlparser import Xmlparser

inputPath = 'data/'
outputFile = 'trainfile.iob'
outputPath = 'data/'
outputFilepath = outputPath+outputFile

parser = Xmlparser(inputPath=inputPath)
res = parser.parse(outputFilepath=outputFilepath, inputPath=inputPath)