
import re

a = 'Moscow is a beautiful city '

if re.search('i*', a):
    print('Got it\n')

if re.search('I*', a):
    print('Hit it \n')

if re.search('s+', a):
    print('Found s\n')

if re.search('l?', a):
    print('Found l \n')

if re.search('^M', a):
    print('Found M\n')

if re.search('y$', a):
    print('Found y \n')
