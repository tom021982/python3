
import sys

try:
    s = input('Enter something --> ')

except EOFError:
    print('\n why did you do an EOF on me?')

except:
    print('\nSome error/exception occurred.')
    # here, we are not exiting the program
    print('Done')
