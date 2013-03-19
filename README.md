Anagram solver
==============

Usage
=====

Database words in plain-text format:
```bash
	$ ./anagrammer.py --database wordlist.txt --format plain myword
```
Database in XML format and using XPath to extract words from the file:
```bash
	$ ./anagrammer.py --database wordlist.xml --xpath ./words myword
```

*Note:* You can give as many words as you want. Anagrams are generator for each words separately.


### Permutations ###
Instead of generating anagrams you can generate permutations for you input words
```bash
	$ ./anagrammer.py --permutations myword
```
**BIG FAT WARNING!**

Generating permutations for long words may take ages and is usually waste of time. Try using short words (less than 5 characters) to get any meaningful output!
