def filereader(filename):
    hashes = {}
    M = 0

    f = open(filename)
    N = int(f.readline())
    imgs = {
        'H': [],
        'V': []
    }

    for i in range(N):
        line = f.readline().split(" ")
        n = int(line[1])
        imgs[line[0]].append([None for _ in range(n+1)])
        print(imgs)
        for j in range(n):
            try:
                imgs[line[0]][-1][j] = hashes[line[j+2].strip()]
            except:
                hashes[line[j+2].strip()] = M
                imgs[line[0]][-1][j] = M
                M += 1
        imgs[line[0]][-1][:-2] = sorted(imgs[line[0]][-1][:-2])
        imgs[line[0]][-1][-1] = i

    imgs['H'].sort(key=len)
    imgs['V'].sort(key=len)

    return hashes, imgs


if __name__ == "__main__":
    print(filereader("testcases/a_example.txt"))