__author__ = 'pelipenko'

import re as re

class Line:
    prefix = ''
    key = ''
    value = ''
    postfix = ''

    def __str__(self):
        return "__str__"

    def __unicode__(self):
         return "__unicode__"

    def __repr__(self):
         return 'prefix:\'{0}\' key:\'{1}\' value:\'{2}\' postfix:\'{3}\'' .format(self.prefix, self.key, self.value, self.postfix)

class Parser:
    def splitLine(self, line):
        if line.isspace():
            return None
        '''
        res = re.search('^(?P<comment>[#;].*)', line)
        l = Line
        if None != res.group('comment'):
            l.prefix = res.group('comment')
        else:
            res = re.search('^(?P<key>([\\S]+))', line)
            if None != res.group('key'):
                l.key = res.group('key')

            res = re.search('^(?P<value>([\\S]+))', line)
            lst = list(line)
            #del lst[0:2]
            #lst.insert(2, '11111')
            return ''.join(lst)

        return l
        '''
        lst = list(line.rstrip('\n'))

        l = Line()
        isComment = False
        sss = ''
        #rc = re.compile(".*\s+(?=[A-Z#])(?!.\s)").split(line)
        #rc = re.findall("\\b[a-z #']*\\w+", line) #.split(line)
        found = re.findall("\\s*[\S]*\S", line)

        #print 'f', found
        if found is not None:
            key = found[0]
            if found[0][0] is '#': #comment detected
                return None #l.prefix = ''.join(rc)
            else:
                l.key = key.strip()
                idx = 0
                for idx, word in enumerate(found):
                    if word.strip()[0] is '#':
                        break
                l.value = ''.join(found[1:idx])
                if idx != len(found):
                    l.postfix = ''.join(found[idx:])
        '''
        sp = line.split()
        if sp[0][0] == '#':
            l.prefix = ''.join(sp)
        else:
            counter = 0
            l.key = sp[0]
            postfix = ''

            for word in sp:
                if word[0] == '#':
                    l.postfix = sp[counter:]
                else:
                    word
                counter += 1

        return l
        '''
        return l


class SettingsParser:

    def __init__(self, filename):
        self._file = open(filename, 'r')
        self._parser = Parser()
        self._settingsDict = dict()

    def readAll(self):
        for idx, line in enumerate(self._file):
            lineObj = self._parser.splitLine(line)
            if lineObj is not None:
                self._settingsDict[idx] = lineObj
        return self._settingsDict

    # replace if key exists
    def set(self, key='', value=''):
        return

    def get(self, key='', value=''):
        return

    def remove(self, key='', value=''):
        return

    def save(self):
        return

if __name__ == "__main__":
    filename = '../examples/simple_config.txt'
    parser = SettingsParser(filename)
    print(parser.readAll())