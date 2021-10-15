import sys, xmnlp, snowNLP_test

class testClass:
    def __init__(self, plainText: str) -> None:
        self.plainText = snowNLP_test.tcToSc(plainText)
        xmnlp.set_model('xmnlp-models')
    
    def getWordSegment(self) -> str:
        return '|'.join(xmnlp.seg(self.plainText))

    def getWordSegmentWithTags(self) -> list:
        return xmnlp.tag(self.plainText)

    def getSentiment(self) -> float:
        return xmnlp.sentiment(self.plainText)[1] # [0] is index of -ve emotion, [1] is for +ve emotion

# following just for testing
if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()

    plainText = snowNLP_test.tcToSc(plainText)
    
    xmnlp.set_model('xmnlp-models')
    s = xmnlp.seg(plainText)
    print('|'.join(s))