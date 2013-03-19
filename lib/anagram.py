from xml.etree import ElementTree as ET


class Anagrammer(object):
    words = []

    def loadDatabase(self, database, xpath=None):
        if xpath is None:
            xpath = './st/s'

        print('Loading %s using XPath %s ' % (database, xpath))

        tree = ET.parse(database)
        root = tree.getroot()

        self.words = [word.text for word in root.findall(xpath)]

        print('%d words found.' % len(self.words))

    def anagrams(self, word):
        print("\nAnagrams for '%s':" % word)
        sword = sorted(word)
        anagrams = [w for w in self.words if sorted(w) == sword]
        if len(anagrams):
            for anagram in anagrams:
                print(anagram)
        else:
            print('No anagrams found :(')
