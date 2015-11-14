# with open("adclog.txt") as fh:
    # coords = [tuple(line.strip("()\n'").split(", ")) for line in fh]
# print(coords)

with open("adclog.txt") as fh:
    coords = []
    for line in fh:
        line = line.strip('()\n')  # Get rid of the newline and  parentheses
        line = line.split(', ')  # Split into two parts
        c = tuple(float(x) for x in line)  # Make the tuple
        coords.append(c)

print [coords]

__author__ = 'colinmacrae'
