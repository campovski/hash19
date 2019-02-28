from filereader import filereader
import algo1


def dist(a, b):
    inter = len(set(a).intersection(set(b)))
    return min([inter, len(a)-inter, len(b)-inter])


def naive(imgsH, imgsV):
    imgsW = algo1.generate_Ws(imgsV)

    nh, nw = len(imgsH), len(imgsW)

    score = 0
    slideshow = [None for _ in range(nh+nw)]
    h, w = 0, 0
    if nh > nw:
        slideshow[0] = imgsH[0]
        h += 1
    else:
        slideshow[0] = imgsW[0]
        w += 1

    for i in range(1, nh+nw):
        if h == nh:
            slideshow[i] = imgsW[w]
            w += 1
            continue
        elif w == nw:
            slideshow[i] = imgsH[h]
            h += 1
            continue

        disth = dist(slideshow[i-1][:-1], imgsH[h][:-1])
        distw = dist(slideshow[i-1][:-1], imgsW[w][:-1])

        if disth > distw:
            slideshow[i] = imgsH[h]
            h += 1
            score += disth
        else:
            slideshow[i] = imgsW[w]
            w += 1
            score += distw

    return slideshow, score


if __name__ == "__main__":
    hashes, imgs = filereader("testcases/b_lovely_landscapes.txt")
    slideshow, score = naive(imgs['H'], imgs['V'])
    print(score)

    with open("out/b.txt", 'w') as f:
        f.write("{}\n".format(len(slideshow)))
        for s in slideshow:
            f.write("{}\n".format(s[-1]))