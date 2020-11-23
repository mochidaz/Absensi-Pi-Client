import sys

args = sys.argv[1]

with open(args, 'r') as f:
    lines = f.readlines()
with open(args, 'w') as f:
    x = []
    for i in lines:
        if '#' in i:
            pass
        else:
            f.write(i)
