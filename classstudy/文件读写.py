import os
print(os.path.exists('guorui.txt'))
print(os.path.isfile('guorui.txt'))

filename='guorui.txt'
lis=[]
with open(filename,'r') as f:
    line=f.readline()
    while line:
        lis.append(line)
        line=f.readline()

print(lis)
