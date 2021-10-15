import sys

import jiagu
import snowNLP_test
import pycantonese_test
import jieba_test
import xmNLP_test
import jiagu_test

if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()
    
    snow = snowNLP_test.testClass(plainText)
    pycanton = pycantonese_test.testClass(plainText)
    jie = jieba_test.testClass(plainText)
    xm = xmNLP_test.testClass(plainText)
    jia = jiagu_test.testClass(plainText)
    
    L = [
        "<<Sentiment Analysis>>",
        "\n\nSnowNLP: " + str(snow.getSentiment()),
        "\nxmNLP: "     + str(xm.getSentiment()),
        "\nJiagu: "     + str(jia.getSentiment()),

        "\n\n<<Word Segment>>",
        "\n\nSnowNLP:\n"     + str(snow.getWordSegment()),
        "\n\nxmNLP:\n"       + str(xm.getWordSegment()),
        "\n\nJiagu:\n"       + str(jia.getWordSegment()),
        "\n\npyCantonese:\n" + str(pycanton.getWordSegment()),
        "\n\nJieba:\n"       + str(jie.getWordSegment()),
        
        "\n\n<<Word Tags>>",
        "\n\nSnowNLP:\n"     + str(snow.getWordSegmentWithTags()),
        "\n\nxmNLP:\n"       + str(xm.getWordSegmentWithTags()),
        "\n\nJiagu:\n"       + str(jia.getWordSegmentWithTags()),
        "\n\npyCantonese:\n" + str(pycanton.getWordSegmentWithTags()),
    ]
    with open('NLP_results.txt', 'w', encoding='utf-8') as outputFile:
        outputFile.writelines(L)

    print("NLP comparison done!!!\n\n")

    '''
    print("\nSnowNLP Sentiment Analysis: ", snow.getSentiment())
    print("\nxmNLP Sentiment Analysis: ", xm.getSentiment())

    print("\nSnowNLP Word Segment:\n", snow.getWordSegment())
    print("\nxmNLP Word Segment:\n", xm.getWordSegment())
    print("\npyCantonese Word Segment:\n", pycanton.getWordSegment())
    print("\nJieba Word Segment:\n", jie.getWordSegment())

    print("\nSnowNLP Word Tags:\n", snow.getWordSegmentWithTags())
    print("\nxmNLP Word Tags:\n", xm.getWordSegmentWithTags())
    print("\npyCantonese Word Tags:\n", pycanton.getWordSegmentWithTags())
    '''