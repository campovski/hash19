from filereader import filereader
from naive import dist
import algo1
import copy
import random

hashes, imgs = filereader("testcases/c_memorable_moments.txt")
ws = algo1.generate_Ws(imgs['V'])

imgs = random.shuffle(imgs['H'] + ws)


N = len(imgs)
score = 0

slideshow = [0 for _ in range(N)]
slideshow[0] = imgs[0]
del(imgs[0])
n = 1
while len(imgs) > 0:
    print(n)
    best = 0
    bd = 0
    for i in range(min(10000,len(imgs))):
        d = dist(slideshow[n-1][:-1], imgs[i][:-1])
        if d >= bd:
            best = i
            bd = d
    slideshow[n] = copy.deepcopy(imgs[best])
    score += bd

    del(imgs[best])
    n += 1

print(score)

with open("out/c.txt", 'w') as f:
    f.write("{}\n".format(len(slideshow)))
    for s in slideshow:
        f.write("{}\n".format(s[-1]))
