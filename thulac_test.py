# thulac library use time.clock() func which has been removed
import time
if not hasattr(time, 'clock'):
    setattr(time,'clock',time.perf_counter)

import sys, thulac

if __name__ == '__main__':
    textFileName = sys.argv[1]
    with open(textFileName, 'r', encoding='utf-8') as textFile:
        plainText = textFile.read()
    
    thu1 = thulac.thulac(seg_only=True)
    s = thu1.cut(plainText, True)
    print("Traditional Chinese:\n", s)

    thu2 = thulac.thulac(seg_only=True, T2S=True)
    s = thu2.cut(plainText, True)
    print("\nSimplified Chinese:\n", s)

    thu3 = thulac.thulac(seg_only=True, T2S=True, filt=True)
    s = thu3.cut(plainText, True)
    print("\nFiltered Chinese:\n", s)