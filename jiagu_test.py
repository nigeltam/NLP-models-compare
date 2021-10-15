import sys, jiagu, snowNLP_test

class testClass:
    def __init__(self, plainText: str) -> None:
        self.plainText = snowNLP_test.tcToSc(plainText) # snowNLP performs better in simp. chin.
        self.words = []
    
    def getWordSegment(self) -> str:
        #return '|'.join(jiagu.seg(self.plainText))

        wordSegment = jiagu.seg(self.plainText)
        def isNotSpace(s): return s != ' '
        self.words = list(filter(isNotSpace, wordSegment))
        return '|'.join(self.words)

    def getWordSegmentWithTags(self) -> list:
        if len(self.words) == 0: self.getWordSegment()
        return jiagu.pos(self.words)

    def getSentiment(self) -> float:
        return jiagu.sentiment(self.plainText)

# following just for running comparison between TC and SC
if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()