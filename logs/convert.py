import os
from tqdm import tqdm

VOCAB_PATH = '/home/share/zh/corpus/PKU-Paraphrase-Bank-master/vocab'

word_dict = {}
idx = 1
with open(VOCAB_PATH, 'r') as f:
    for line in f.readlines():
        word_dict[line.strip().split(' ')[0]] = idx
        idx += 1

for root, dis, files in os.walk('.'):
    for file in tqdm(files):
        if not file.endswith('txt'):
            continue
        filename = os.path.join(root, file)
        new_data = []
        with open(filename, 'r') as f:
            for word in f.readline().strip().split(' '):
                if word in word_dict.keys():
                    new_data.append(str(word_dict[word]))
                else:
                    new_data.append('0')
        with open(filename, 'w') as f:
            f.write(' '.join(new_data))

