# 2 - masala
def juft_boluvchi(n):
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            yield i


# n = int(input(('son kiriting: ')))
# j = juft_boluvchi(n)
# print(next(j))
# print(next(j))

# 3 - masala
def tub_sonlar(a):
    for i in range(1, a+1):
        c = 0
        for k in range(1, i):
            if i % k == 0:
                c += 1
        if c == 1:
            yield i


# a = int(input('son kiriting: '))
# t = tub_sonlar(a)
# print(next(t))
# print(next(t))



# 4 - masala
def tub_boluvchi(n):
    tub = []
    for j in range(1, n+1):
        if n % j == 0:
            tub.append(j)
    for i in tub:
        c = 0
        for k in range(1, i):
            if i % k == 0:
                c += 1
        if c == 1:
            yield i


# n = int(input('son kiriting: '))
# t = tub_boluvchi(n)
# print(next(t))
# print(next(t))


# 5-masala
def juft_son(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i


# n = int(input('son kiriting: '))
# t = juft_son(n)
# print(next(t))
# print(next(t))


# 6 - masala
def find_length(text):
    result = text.split()
    for i in result:
        yield i, len(i)


# f = find_length("Python is a powerful programming language that is easy to learn.")
# print(next(f))
# print(next(f))


# 7 - masala
def find_length_words(text):
    result = text.split()
    for i in result:
        if len(i) > 5:
            yield i


# f = find_length_words("Python is a powerful programming language that is easy to learn.")
# print(next(f))
# print(next(f))


# 8 - masala

def count_numbers(l):
    r = {}
    for i in l:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1

    for n, count in r.items():
        if count == 3:
            yield n


# c = count_numbers([1, 2, 3, 2, 4, 5, 6, 4, 4, 7, 2, 5, 7, 8, 7, 9])
# print(next(c))
# print(next(c))
# print(next(c))




