import sys, pycantonese

class testClass:
    def __init__(self, plainText: str) -> None:
        self.plainText = plainText
    
    def getWordSegment(self) -> str:
        return '|'.join(pycantonese.segment(self.plainText))

    def getWordSegmentWithTags(self) -> list:
        return pycantonese.pos_tag(pycantonese.segment(self.plainText))

# following just for testing
if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()
    
    s = pycantonese.segment(plainText)
    print(s)