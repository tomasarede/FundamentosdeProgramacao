a = ((1,1),(1,2))
b = ((1,2),(1,3))
pos1_a = None
pos1_b = None
for l in a:
    pos1_a = l
    break
for c in b:
    pos1_b = c
    break

print(pos1_a,pos1_b)