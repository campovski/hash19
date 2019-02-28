def filereader(filename):
    hashes = {}
    imgs = None
    M = 0

    f = open(filename)
    N = int(f.readline())
    imgs = [None for _ in range(N)]

    for i in range(N):
        line = f.readline().split(" ")
        n = int(line[1])
        imgs[i] = [None for _ in range(n+1)]
        for j in range(int(n)):
            try:
                imgs[i][j] = hashes[line[j+2].strip()]
            except:
                hashes[line[j+2].strip()] = M
                imgs[i][j] = M
                M += 1
        imgs[i][-1] = line[0]
        imgs[i][:-1] = sorted(imgs[i][:-1])

    return hashes, imgs


if __name__ == "__main__":
    print(filereader("testcases/a_example.txt"))