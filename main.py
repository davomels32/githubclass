import re

hand = open ('doc.txt')
for line in hand:
        line = line.rstrip()
            if re.search('lorem', line):
                print (line)
            if line.find ('lorem') >=0:
                print (line)
            if re.search('^lorem', line):
                print (line)
                                                            #if line.startswith('lorem', line):
                                                                   # print (line)

