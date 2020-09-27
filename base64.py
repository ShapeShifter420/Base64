TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode(text):
    result = ''
    c = 0
    l = len(text)
    A = []
    A2 = []
    tmp = ''
    for t in range(l):
        A.append(bin(int(ord(text[t]))))
        A[t] = A[t][2:]
        if len(A[t]) != 8:
            while len(A[t]) != 8:
                A[t] = '0' + A[t]
    for t in A:
        tmp += t
    z = len(tmp) % 24
    if z != 0:
        while z != 0:
            tmp += '0'
            c += 1
            z = len(tmp) % 24
    for t in range(int(len(tmp) / 6)):
        A2.append(tmp[t * 6:t * 6 + 6])
        A2[t] = int(A2[t], 2)
    for t in A2:
        result += TABLE[t]
    if c / 6 > 1:
        c = int(c)
        t = int(c / 6)
        E = '=' * t
        result = result[0:-t] + E
    print(result)


if __name__ == '__main__':
    text = input("input: ")
    encode(text)
