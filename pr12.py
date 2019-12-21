# dictionary example

capitals = { 'India' : 'New Delhi',
             'UK' : 'London',
             'Germany' : 'Berlin',
             'France' : 'Paris',
             'Bhutan' : 'Thimphu',
             'Russia' : 'Moscow' }

# Fetching a value based on key
print('\n The capital of Bhutan is : %s' %capitals['Bhutan'])

# Adding {keys} : {value} Pair
capitals['Japan'] = 'Tokyo'

print('\n There are %d pairs in the dictionary' %len(capitals))

# Delete a Pair
del capitals['UK']

print('\n Now, there are %d pairs in the dictionary \n' %len(capitals))

# List of key:Value Pairs

for country, capital in capitals.items():
    print('Capital of %s is %s ' %(country, capital))
