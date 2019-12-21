# RedEx Script

import re  # RedEx module.

regex = r"([a-zA-Z]+) (\d+)" # regex search/match definition
if re.search(regex, "April 18"):
    match = re.search(regex, "April 18")
    print("Match at index %s, %s" %(match.start(), match.end()))
# Use MatchObject's start() and end() methods to retrieve the positions

    print("Full match: %s" %(match.group(0)))
    print("Month: %s" %(match.group(1)))
    print("Day %s" %(match.group(2)))
else:
    print("The regex pattern does not match. :(")
