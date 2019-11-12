# import pandas as pd

x = []
i = 0
with open('aparc.a2009s+aseg.txt') as f:
    for line in f:
        row = line.strip().split()
        row[0] = str(i)
        x.append('\t'.join(row))
        i+=1

with open('aparc.a2009s+aseg_new.txt', 'w+') as f:
    f.write('\n'.join(x))
    f.write('\n')
