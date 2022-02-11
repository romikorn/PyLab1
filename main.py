import re
file = open('steam_description_data.csv',  encoding='utf8')
words = 0
symbols = 0
symbols_NoSpace = 0
symbols_NoComma = 0
symbols_NoDot = 0
symbols_NoMarks = 0
symbols_NoExclamation = 0
symbols_NoColon = 0
comma = 0
dot = 0
exclamation = 0
colon = 0
sentence = 0
for line in file:
    list0 = line.split()
    list1 = line.split(',')
    list2 = line.split('.')
    list3 = line.split('!')
    list4 = line.split(':')
    list5 = re.split(r'[,\!]', line)
    symbols += len(line)
    words += len(list0)
    symbols_NoSpace += sum(len(word) for word in list0)
    symbols_NoComma += sum(len(word) for word in list1)
    symbols_NoDot += sum(len(word) for word in list2)
    symbols_NoExclamation += sum(len(word) for word in list3)
    symbols_NoColon += sum(len(word) for word in list4)
    sentence += len(list5)
comma = symbols - symbols_NoComma
dot = symbols - symbols_NoDot
exclamation = symbols - symbols_NoExclamation
colon = symbols - symbols_NoColon
symbols_NoMarks = symbols - dot - comma - exclamation - colon
print(' Количество символов без знаков препинания:',symbols_NoMarks,'\n',
      'Количество слов:',words,'\n',
      'Количество символов:',symbols,'\n',
      'Количество симоволов без пробелов:', symbols_NoSpace,'\n',
      'Количество предложений:',sentence)
file.close()