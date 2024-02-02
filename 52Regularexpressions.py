import re
mystr = '''The minus sign (-) in the 
above equation also 
suggests that the inverting 
amplifier also provides 
45623 - 234
4515615656 - 6515151515
with a phase shift, and that 
too, makes the signal go 
completely out of phase 
with its original
counterpart'''
# pattern = re.compile(r"original")
# pattern = re.compile(r".")
# pattern = re.compile(r".o")
# pattern = re.compile(r"^The")
# pattern = re.compile(r"^minus")
# pattern = re.compile(r"part$")
# pattern = re.compile(r"counter$")
# pattern = re.compile(r"ug*")
# pattern = re.compile(r"u*g*")
# pattern = re.compile(r"ug{2}")
# pattern = re.compile(r"ug{2}|inverting")
# pattern = re.compile(r"\AThe")
# pattern = re.compile(r"\Aoriginal")
# pattern = re.compile(r"\bwi")
# pattern = re.compile(r"al\b")
pattern = re.compile(r"\d{5} - \d{3}")
matches = pattern.finditer(mystr)
print(matches)
for match in matches:
    print(match)