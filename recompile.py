
import re

# Pre-compile the pattern
regexes = [re.compile(p) for p in ['this','that',]]

text = 'Does this text match the pattern?'

for regex in regexes:
    print('Looking for "%s" in "%s" ->' %(regex.pattern, text)),

    if regex.search(text):
        print('found a match!')
    else:
        print('no match')
