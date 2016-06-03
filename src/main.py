__author__ = 'pelipenko'
import re
import fileinput

class Line:
    key = ''
    value = ''
    postfix = ''

    def __str__(self):
        return "__str__"

    def __unicode__(self):
         return "__unicode__"

    def __repr__(self):
         return 'prefix:\'{0}\' key:\'{1}\' value:\'{2}\' postfix:\'{3}\'' .format(self.key, self.value, self.postfix)

class Parser:
    def split_line(self, line):
        if line.isspace():
            return None

        lst = list(line.rstrip('\n'))

        l = Line()
        isComment = False
        #found = re.findall("\\s*[\S]*\S", line)
        found = re.compile("^\s*(\b[a-zA-Z0-9]+)\s*", line)

        print 'f', found
        if len(found) != 0:
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
        return l

    def generateLine(self, line = Line()):
        return '{0} {1} {2}'.format(line.key, line.value, line.postfix)

class SettingsParser:
    def __init__(self, filename):
        self._filename = filename
        self._parser = Parser()
        self._settingsDict = dict()
        self._keyValueDict = dict()
    '''
    def memory_read_all(self):
        with open(self._filename, 'r') as file:
            for idx, line in enumerate(file):

    '''

    def read_all(self):
        with open(self._filename, 'r') as file:
            for idx, line in enumerate(file):
                line_obj = self._parser.split_line(line)
                if line_obj is not None:
                    self._settingsDict[idx] = line_obj
                    self._keyValueDict[line_obj.key] = line_obj.value
        return self._keyValueDict

    # replace if key exists
    def set(self, key='', value='', saveToFile = False):
        self._keyValueDict[key] = value
        if saveToFile:
            self.save(key)
        return

    '''
    def get(self, key='', value=''):
        with open(self._filename, 'r') as file:
            for idx, line in enumerate(file):
        return
    '''

    def remove(self, key_to_remove='', remove_all_line = False):
        key_was_removed = False
        for line in fileinput.input(self._filename, inplace=True, mode='r'):
            key_was_removed = False
            strip_line = line.strip()
            lineObj = self._parser.split_line(strip_line)
            if lineObj is not None:
                if lineObj.key == key_to_remove:
                    if not remove_all_line:
                        lineObj.key = ''
                        lineObj.value = ''
                        print self._parser.generateLine(lineObj)

                    key_was_removed = True
            if not key_was_removed:
                print strip_line
        '''
        if not key_was_removed:
            raise ValueError("Key was not found")
        '''
        # if keyToSave save only key
        return

    def save(self, key_to_save='', value_to_save=''):
        for line in fileinput.input(self._filename, inplace=True, mode='r'):
            line_was_printed = False
            strip_line = line.strip()
            lineObj = self._parser.split_line(strip_line)
            if lineObj is not None:
                if lineObj.key == key_to_save:
                    lineObj.value = value_to_save
                    print self._parser.generateLine(lineObj)
                    line_was_printed = True
            if not line_was_printed:
                print strip_line
        # if keyToSave save only key
        return



# let's try to create a sequence of objects, like list:
#
# key value for key #comment
# # comment2
#
# key2
#
# Will transform to:
# KeyValuePairWithComment("key", "value for key", "comment")
# Comment("comment2")
# EmptyString()
# KeyValuePair("key2", "")
# EmptyString()

class Comment:
    def __init__(self,text=''):
        self.text = text
    text = ''
    def __repr__(self):
        return "Comment:'{0}'".format(self.text)

class KeyValue:
    key = ''
    value = ''

class KeyValueWithComment:
    key = ''
    value = ''
    comment = Comment
    def __repr__(self):
        return "KeyValuePairWithComment: '{0}' '{1}' '{2}'".format(self.key, self.value, self.comment.text)

class EmptyString:
    text = ''
    def __repr__(self):
        return "EmptyString: ''"

class NotValidString:
    text = ''
    def __repr__(self):
        return "NotValidString: '{0}'".format(self.text)


class FileSerializer:
    def _parse_line(self, line=''):
        if line.isspace():
            return EmptyString()

        found = re.findall("\\s*[\S]*\S", line)

        if len(found) != 0:
            if found[0][0] is '#': #comment detected
                return Comment(line.strip())
            else:
                pair = KeyValueWithComment()
                pair.key = found[0].strip()
                idx = 0
                for idx, word in enumerate(found):
                    if word.strip()[0] is '#':
                        break
                pair.value = ''.join(found[1:idx])
                if idx != len(found):
                    pair.comment = Comment(''.join(found[idx:]))

                return pair
        return NotValidString(line)

    def read_file(self, filename):
        serialized_object_list = list()
        with open(filename, 'r') as file:
            for line in file:
                serialized_object_list.append(self._parse_line(line))

        return serialized_object_list

class SettingsParser2:
    def __init__(self, filename):
        self._filename = filename
        serializer = FileSerializer()
        serializer.read_file(filename)
        self._settingsDict = dict()
        self._keyValueDict = dict()

    # returns list of KeyValues
    # maybe return without comments?
    def read_all_keys(self):
        return

    # returns KeyValue by key
    # reads from end of file
    #
    # alg:
    # open file, read line by line while didn't get our value
    def get(self,key=''):
        return

    # replace KeyValue in file
    # reads from end of file
    #
    # alg:
    # open file, read line by line while didn't get our value
    # when get replace value
    # if not get add KeyValue to end of file
    def set(self, key_value=KeyValue()):
        return

    # remove key with value from file
    # reads from end of file
    #
    # alg:
    # open file, read line by line while didn't get our value
    # when found remove all line
    def remove(self, key=''):
        return

if __name__ == "__main__":
    pass
    #filename = '../examples/simple_config.txt'
    #parser = SettingsParser(filename)
    #print parser.read_all()
    #parser.remove('key1', True)
    #print parser.read_all()
    #parser.save('key1', 'HELLO! world orgjeoir e jgperojg perj gper ')
    #parser.remove('key1', True)



