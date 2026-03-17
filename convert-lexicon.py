# Copyright (C) 2025 Information and Press Service of the Government of Luxembourg 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Just converts from your lexicon to spaced-separated Foma format, which Foma processes very quickly even if there are a lot of entries.
# Takes the input lexicon as an argument and saves lex.txt in the current directory.
# Normalization step: only keep upper-case entries if they differ from corresponding lower-case entries, convert to lower case otherwise.
# Print words with multiple pronunciations for debugging purpuses.

from sys import argv

from collections import defaultdict
lex=defaultdict(set)

with open(argv[1], encoding="utf-8") as fin:
    for line in fin:
        if len(line.strip().split())<2:
            print('ERR:'.line);
            continue
  #      print(line)
        word, pron=line.strip().split("\t")
        word=word.strip()
        pron=" ".join(["/{}".format(ph) for ph in pron.strip().split()])
        lex[word].add(pron)

words=set(lex.keys())

for word in words:
    lword=word.lower()
    if word==lword:
        continue
    if lword not in lex:
        lex[lword]=lex[word]
    if lex[word]==lex[lword]:
        del lex[word]
        continue

with open("lex.txt", "w", encoding="utf-8") as fout:
    for word, prons in sorted(lex.items()):
        if len(prons)>1:
            print(word)
        pron=sorted(prons)[0]
        fout.write(" ".join(word)+"\n")
        fout.write(pron+"\n")
