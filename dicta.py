
states = {

    'TN' : {
        'capital': 'Chennai',
        'Language': 'Tamil'
      },


    'Kerela' : {
         'capital': 'Trivamdrum',
         'Language': 'Malayalam'
       },

    'Karnataka' : {
         'capital': 'Bangalore',
         'Language': 'Kannada'
      }
    }

labels = {
   'capital': 'Capital City',
   'Language': 'Spoken Language'
    }

# which state to choose ?
state = input("State : " )

# fetch capital or language for the chosen state ?
fetch = input("Capital (C) or Language (L) ? ")

if fetch == 'C' : key = 'capital'
if fetch == 'L' : key = 'Language'

if state in states: print("%s 's %s is %s." % (state, labels[key], states[state][key]))
