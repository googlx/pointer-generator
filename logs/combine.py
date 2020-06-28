import os
import glob
import pandas as pd
from tqdm import tqdm

columns = ['decoded', 'reference']
df = pd.DataFrame(columns=columns)

text = []
with open('test.txt', 'r') as f:
    idx = 0
    for line in f.readlines():
        line = line.strip()
        if idx%2 == 0:
            text.append(''.join(line.split(' ')))
        idx += 1

size = len(glob.glob('decoded/[0-9]*_decoded.txt'))

data = []
for idx in tqdm(range(size)):
    item = {}
    for col in columns:
        fn = col+ '/{0:06d}'.format(idx) + f'_{col}.txt'
        with open(fn, 'r') as f:
            item[col] = f.read().strip()
    decoded = ''.join(item['decoded'].split(' '))
    reference = ''.join(item['reference'].split(' '))
    data.append(f'{text[idx]}\t{decoded}\t{reference}')

with open('pred.tsv', 'w') as f:
    f.write('\n'.join(data))
