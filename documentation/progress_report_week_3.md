# Week3 progress report

I added testing documentation file. After discussion with teacher I decided to make melody instead of just using chords, and start with using notes of the same length for a start (not considering rhythm). I googled ABC notes that could be used as a base. I decided to make a script that downloads them based on key (so that I don't have to do it manually). 
Time spent: 1 h

I ended up using files with multiple abc notes in single file instead (and not make a script for downloading).
Time spent: 2 h

Use parser library for parsing abc notes. It gives key and notes in a way that can be inserted into Trie. Experiment to find out if the way that notes come out of the parser can be played with pygame - yes, they can.
Time spent: 1 h

Experiment with inserting abc notes parsed into Trie. Add preliminary testing implementation of this.
Time spent: 1 h

Turn note logic into a class. Add one unit test. try to get python coverage to cover src/logic still (is not covering it).
time spent: 2 h

Add tasks.py to make coverage work. Made it to a situation that it covers EVERYTHING now so not perfect (would like it to cover only code parts) but at least this is better than it covering just one file which it did before.
Time spent: 1 h

Total time spent: 8 h