import itertools

from xml.etree import ElementTree as ET


class Anagrammer(object):
    words = []

    def loadDatabase(self, database, format, xpath=None):
        if xpath is None:
            xpath = './st/s'

        if format == 'xml':
            print('Loading %s in XML format using XPath %s ' % (database, xpath))
            tree = ET.parse(database)
            root = tree.getroot()
            self.words = [word.text.lower() for word in root.findall(xpath)]
        elif format == 'plain':
            print('Loading %s in plain-text format')
            file = open(database, 'r')
            self.words = [line.strip().lower() for line in file.readlines()]
            file.close()
        else:
            raise TypeError('Format %s is not supported.' % format)

        print('%d words found.' % len(self.words))

    def anagrams(self, word):
        word = word.strip().lower()
        print("Anagrams for '%s':" % word)
        sword = sorted(word)
        anagrams = [w for w in self.words if sorted(w) == sword]
        if len(anagrams):
            for anagram in anagrams:
                print(anagram)
        else:
            print('No anagrams found :(')

    def permutations(self, word):
        print('Permutations for word %s' % word)
        r = len(word)
        combos = (''.join(combo) for combo in itertools.permutations(word, r))
        for combo in combos:
            print(combo)

