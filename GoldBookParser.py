#-*-coding:UTF-8-*-
import re

intI = 0
fileGoldBook = open('goldbook.txt')

linesGoldBook = fileGoldBook.readlines()
# print linesGoldBook[8438]

intLenLinesGoldBook = linesGoldBook.__len__()
setInstance = set()

patternIndex = re.compile('(.+),\s(\d)')
'''
line = linesGoldBook[13]
# line = 'α-addition (alpha-addition), 2'
line = line.replace('\n', '')
line = line.replace('\x0C', '')
match = patternIndex.search(line)
print 'test'
if match:
    print 'yes'
else:
    print 'no'
'''


strTmp = ''
listRange = linesGoldBook[10:8434]
for line in listRange:
    # line = linesGoldBook[intFlag]
    line = line.replace('\n', '')
    line = line.replace('\x0C', '')
    strTmp += line
    match = patternIndex.search(strTmp)
    if match:
        setInstance.add(match.group(1))
        strTmp = ''
    else:
        strTmp += ' ' + line

print setInstance.__len__()

listRange = linesGoldBook[8438:]
fileInstances = open('Instances', 'w')
strTmp = ''
flagSource = False
intCount = 0
print listRange[0]
for line in listRange:
    line = line.replace('\n', '')
    line = line.replace('\x0C', '')
    if line.find('IUPAC Compendium of Chemical Terminology') != -1:
        continue
    if line.find('of 1622') != -1:
        continue
    if line in setInstance:
        strTmp += line + '\n'
        flagSource = False
    else:
        if line.find('Source:') != -1:  # find, 'Source:' in line
            fileInstances.write(strTmp + '\n')
            fileInstances.write('\n')
            intCount += 1
            strTmp = ''
            flagSource = True
        else:  # not find
            if flagSource == True:
                continue
            else:
                strTmp += line
print intCount

for intFlag in range(8438, intLenLinesGoldBook):
    line = linesGoldBook[intFlag]

    intFlag += 1



'''
for lineGoldBook in linesGoldBook:
    # print lineGoldBook
    lineGoldBook = lineGoldBook.replace('\n', '')
    lineGoldBook = lineGoldBook.replace('\x0C', '')
    if lineGoldBook == 'Index':
        print 'yes'
    print lineGoldBook
    intI += 1
    if intI > 10:break

'''
