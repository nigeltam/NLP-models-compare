from snownlp import SnowNLP
import sys

def tcToSc(text: str) -> str:
    s = SnowNLP(text)
    return s.han

class testClass:
    def __init__(self, plainText: str) -> None:
        self.plainText = tcToSc(plainText) # snowNLP performs better in simp. chin.
        self.processedObject = SnowNLP(self.plainText)
    
    def getWordSegment(self) -> str:
        return '|'.join(self.processedObject.words)

    def getWordSegmentWithTags(self) -> list:
        return list(self.processedObject.tags)

    def getSentiment(self) -> float:
        return self.processedObject.sentiments


# following just for running comparison between TC and SC
if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()
    
    s = SnowNLP(plainText)
    print("Traditional Chinese:\n", s.words)

    s = SnowNLP(s.han)
    print("\nSimplified Chinese:\n", s.words)