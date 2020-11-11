import os
import bisect
import itertools
import random

import nltk
from konlpy.corpus import kolaw
from konlpy.tag import Okt # 변경해도 무방

data_dir = './data/'

files = [data_dir + file for file in os.listdir(data_dir)  if os.path.isfile(data_dir + file) ]
for f in files:
  print (f)

doc = '\n'.join([ open(file, encoding='utf8').read()
    for file in files
    ])

def generate_sentence(cfdist, word):
    sentence = []
    for i in range(0, 100): # 변경해도 무방
        sentence.append(word)
        choices, weights = zip(*cfdist[word].items())
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        word = choices[bisect.bisect(cumdist, x)]

    return ' '.join(sentence)


def calc_cfd(doc):
    words = [w for w, t in Okt().pos(doc)]
    bigrams = nltk.bigrams(words)
    return nltk.ConditionalFreqDist(bigrams)


nsents = 1 # 몇 개 만들지
initstr = input('inputstr: ')
print('Loaded {} length sentance.'.format(len(doc)))
cfd = calc_cfd(doc)

for i in range(nsents):
    print('%d. %s' % (i, generate_sentence(cfd, initstr)))