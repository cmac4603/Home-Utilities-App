
def getvoltages(file):
    with open (file, "r") as myfile:
        data = myfile.read().replace("\n", ", ")
    print("[" + data + "]")

getvoltages("adclog.txt")

__author__ = 'colinmacrae'
