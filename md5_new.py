from math import sin, floor

def ascii(symbol):
    code = bin(ord(symbol))[2:]
    if len(code) < 8:
        code = '0' * (8 - len(code)) + code
    return code


def forming(line):
    big_line = '1'
    for letter in line:
        big_line += ascii(letter)
    #big_line += ''
    while len(big_line) % 512 != 448:
        big_line += '0'
    help_line = bin(len(line))[2:]
    while len(help_line) % 8 != 0:
        help_line += '0'
    big_line += (64 - len(help_line)) * '0' + help_line
    return big_line


def F(x, y, z):
    x, y, z = int(x, 16), int(y, 16), int(z, 16)
    go = (x & y) | (~x & z)
    go = hex(abs(go))[2:]
    return '0' * (8 - len(go)) + go

def G(x, y, z):
    x, y, z = int(x, 16), int(y, 16), int(z, 16)
    go = (x & z) | (y & (~z))
    go = hex(abs(go))[2:]
    return '0' * (8 - len(go)) + go

def H(x, y, z):
    x, y, z = int(x, 16), int(y, 16), int(z, 16)
    go = x ^ y ^ z
    go = hex(abs(go))[2:]
    return '0' * (8 - len(go)) + go


def I(x, y, z):
    x, y, z = int(x, 16), int(y, 16), int(z, 16)
    go = y ^ (x | (~z))
    go = hex(abs(go))[2:]
    return '0' * (8 - len(go)) + go


def left_shit(line, s):
    line_new = ''
    for i in line:
        bin_i = bin(int(i, 16))[2:]
        line_new += '0' * (4 - len(bin_i)) + bin_i
    ret = line_new[s:] + line_new[:s]
    aboba = hex(int(ret, 2))[2:]
    return '0' * (8 - len(aboba)) + aboba


def modular_addition(a, b):
    a, b = int(a, 16), int(b, 16)
    z = hex((a + b) % (2 ** 32))[2:]
    return '0' * (8 - len(z)) + z

def Round1(a, b, c, d, k, i, M, T, s):
    f1 = modular_addition(a, F(b, c, d))
    f2 = modular_addition(f1, M[k])
    f3 = modular_addition(f2, T[i-1])
    f4 = left_shit(f3, s)
    return modular_addition(b, f4)


def Round2(a, b, c, d, k, i, M, T, s):
    f1 = modular_addition(a, G(b, c, d))
    f2 = modular_addition(f1, M[k])
    f3 = modular_addition(f2, T[i-1])
    f4 = left_shit(f3, s)
    return modular_addition(b, f4)


def Round3(a, b, c, d, k, i, M, T, s):
    f1 = modular_addition(a, H(b, c, d))
    f2 = modular_addition(f1, M[k])
    f3 = modular_addition(f2, T[i-1])
    f4 = left_shit(f3, s)
    return modular_addition(b, f4)


def Round4(a, b, c, d, k, i, M, T, s):
    f1 = modular_addition(a, I(b, c, d))
    f2 = modular_addition(f1, M[k])
    f3 = modular_addition(f2, T[i-1])
    f4 = left_shit(f3, s)
    return modular_addition(b, f4)


X = forming("Here is a hash by MD5")
M = ['0' * (8 - len(hex(int(X[i: i + 32], 2))[2:])) + hex(int(X[i: i + 32], 2))[2:] for i in range(0, len(X), 32)]
T = ['0' * (8 - len(hex(int(abs(sin(i)) * 2 ** 32))[2:])) + hex(int(abs(sin(i)) * 2 ** 32))[2:] for i in range(1, 65)]
A, B = '01234567', '89abcdef'
D, C = A[::-1], B[::-1]

AA = A
BB = B
CC = C
DD = D


# ROUND1
A = Round1(A, B, C, D, 0, 1, M, T, 7)
A = Round1(A, B, C, D, 4, 5, M, T, 7)
A = Round1(A, B, C, D, 8, 9, M, T, 7)
A = Round1(A, B, C, D, 12, 13, M, T, 7)

B = modular_addition(B, A)


D = Round1(D, A, B, C, 1, 2, M, T, 12)
D = Round1(D, A, B, C, 5, 6, M, T, 12)
D = Round1(D, A, B, C, 9, 10, M, T, 12)
D = Round1(D, A, B, C, 13, 14, M, T, 12)

A = modular_addition(A, D)

C = Round1(C, D, A, B, 2, 3, M, T, 17)
C = Round1(C, D, A, B, 6, 7, M, T, 17)
C = Round1(C, D, A, B, 10, 11, M, T, 17)
C = Round1(C, D, A, B, 14, 15, M, T, 17)

D = modular_addition(D, C)

B = Round1(B, C, D, A, 3, 4, M, T, 22)
B = Round1(B, C, D, A, 7, 8, M, T, 22)
B = Round1(B, C, D, A, 11, 12, M, T, 22)
B = Round1(B, C, D, A, 15, 16, M, T, 22)

C = modular_addition(C, B)


# ROUND2
A = Round2(A, B, C, D, 1, 17, M, T, 5)
A = Round2(A, B, C, D, 5, 21, M, T, 5)
A = Round2(A, B, C, D, 9, 25, M, T, 5)
A = Round2(A, B, C, D, 13, 29, M, T, 5)

B = modular_addition(B, A)

D = Round2(D, A, B, C, 6, 18, M, T, 9)
D = Round2(D, A, B, C, 10, 22, M, T, 9)
D = Round2(D, A, B, C, 14, 26, M, T, 9)
D = Round2(D, A, B, C, 2, 30, M, T, 9)

A = modular_addition(A, D)

C = Round2(C, D, A, B, 11, 19, M, T, 14)
C = Round2(C, D, A, B, 15, 23, M, T, 14)
C = Round2(C, D, A, B, 3, 27, M, T, 14)
C = Round2(C, D, A, B, 7, 31, M, T, 14)

D = modular_addition(D, C)

B = Round2(B, C, D, A, 0, 20, M, T, 20)
B = Round2(B, C, D, A, 4, 24, M, T, 20)
B = Round2(B, C, D, A, 8, 28, M, T, 20)
B = Round2(B, C, D, A, 12, 32, M, T, 20)

C = modular_addition(C, B)


# ROUND3
A = Round3(A, B, C, D, 5, 33, M, T, 4)
A = Round3(A, B, C, D, 1, 37, M, T, 4)
A = Round3(A, B, C, D, 13, 41, M, T, 4)
A = Round3(A, B, C, D, 9, 45, M, T, 4)

B = modular_addition(B, A)

D = Round3(D, A, B, C, 8, 34, M, T, 11)
D = Round3(D, A, B, C, 4, 38, M, T, 11)
D = Round3(D, A, B, C, 0, 42, M, T, 11)
D = Round3(D, A, B, C, 12, 46, M, T, 11)

A = modular_addition(A, D)

C = Round3(C, D, A, B, 11, 35, M, T, 16)
C = Round3(C, D, A, B, 7, 39, M, T, 16)
C = Round3(C, D, A, B, 3, 43, M, T, 16)
C = Round3(C, D, A, B, 15, 47, M, T, 16)

D = modular_addition(D, C)

B = Round3(B, C, D, A, 14, 36, M, T, 23)
B = Round3(B, C, D, A, 10, 40, M, T, 23)
B = Round3(B, C, D, A, 6, 44, M, T, 23)
B = Round3(B, C, D, A, 2, 48, M, T, 23)

C = modular_addition(C, B)

# ROUND4
A = Round4(A, B, C, D, 0, 49, M, T, 6)
A = Round4(A, B, C, D, 12, 53, M, T, 6)
A = Round4(A, B, C, D, 8, 57, M, T, 6)
A = Round4(A, B, C, D, 4, 61, M, T, 6)

B = modular_addition(B, A)

D = Round4(D, A, B, C, 7, 50, M, T, 10)
D = Round4(D, A, B, C, 3, 54, M, T, 10)
D = Round4(D, A, B, C, 15, 58, M, T, 10)
D = Round4(D, A, B, C, 11, 62, M, T, 10)

A = modular_addition(A, D)

C = Round4(C, D, A, B, 14, 51, M, T, 15)
C = Round4(C, D, A, B, 10, 55, M, T, 15)
C = Round4(C, D, A, B, 6, 59, M, T, 15)
C = Round4(C, D, A, B, 2, 63, M, T, 15)

D = modular_addition(D, C)

B = Round4(B, C, D, A, 5, 52, M, T, 21)
B = Round4(B, C, D, A, 1, 56, M, T, 21)
B = Round4(B, C, D, A, 13, 60, M, T, 21)
B = Round4(B, C, D, A, 9, 64, M, T, 21)

C = modular_addition(C, B)

# LAST CALCULATIONS

A = modular_addition(A, AA)
B = modular_addition(B, BB)
C = modular_addition(C, CC)
D = modular_addition(D, DD)



print(A + B + C + D)
