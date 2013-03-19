#!/usr/bin/env python
"""
Copyright (C) 2013 Tomi Pajunen <tomi@madlab.fi>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  LICENSE
"""

import argparse

from lib import Anagrammer


class WordAction(argparse.Action):
    def __call__(self, parser, args, values, options = None):
        args.words = values
        if not args.permutations:
            print("no comb...")
            if not args.database:
                parser.error('You need to specify database')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find anagrams for given words')
    parser.add_argument('--database',
                        help='XML file containing list of words')
    parser.add_argument('--xpath', help='XPath used to find words from XML')
    parser.add_argument('--format', default='xml', help='Database format')
    parser.add_argument('--permutations', action='store_true',
                        help='Print permutations instead of finding anagrams. Warning! Do not use long words!')
    parser.add_argument('words', type=str, nargs='+',
                        action=WordAction,
                        help='Find anagrams for given word(s)')

    args = parser.parse_args()

    grammer = Anagrammer()

    for word in args.words:
        if args.permutations:
            grammer.permutations(word)
        else:
            grammer.loadDatabase(args.database, args.format, args.xpath)
            grammer.anagrams(word)
