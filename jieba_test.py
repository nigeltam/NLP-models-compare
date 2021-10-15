import sys, jieba

class testClass:
    def __init__(self, plainText: str) -> None:
        self.plainText = plainText
        jieba.set_dictionary("jieba_dict/dict.txt.big.txt")
    
    def getWordSegment(self) -> str:
        wordSegment = jieba.cut(self.plainText, cut_all=False)
        def isNotSpace(s): return s != ' '
        wordSegment = list(filter(isNotSpace, wordSegment))
        return '|'.join(wordSegment)

# following for testing only
if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()
    seg_list = jieba.cut(plainText, cut_all=False)
    print("No Dict Mode:\n" + "/ ".join(seg_list))

    jieba.set_dictionary("jieba_dict/dict.txt.big.txt")
    seg_list = jieba.cut(plainText, cut_all=False)
    print("\nDict Mode:\n" + "/ ".join(seg_list))