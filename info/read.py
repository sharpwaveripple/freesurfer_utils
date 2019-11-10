# import pandas as pd

x = []
with open('destrieux.txt') as f:
    for line in f:
        row = line.strip().split()
        x.append('\t'.join(row))

# with open('destrieux_new.txt', 'w+') as f:
#     f.write('\n'.join(x))
#     f.write('\n')
