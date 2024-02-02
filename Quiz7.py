"""Program to find Indian phone numbers from a string"""
import re
mystr = '''Hello! This is a list of phone numbers:
        +919811808695
        0114567821279
        4594516556
        +918512808695
        +919818262563
        4454516512
        +919953529251'''
pattern = re.compile(r"\+91\d{10}")
matches = pattern.finditer(mystr)
for match in matches:
    print(match)