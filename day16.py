# day-16 Q60
# def f(n):
#     if n == 0:
#         return 0
#     return f(n-1) + 100


# n = int(input())
# print(f(n))

# n = int(input())
# def f(x): return f(x-1)+100 if x > 0 else 0


# print(f(n))


# day-16 Q61
# def f(n):
#     if n < 2:
#         return n
#     return f(n-1) + f(n-2)


# n = int(input())
# print(f(n))

# n = int(input())
# def f(x): return 0 if x == 0 else 1 if x == 1 else f(x-1)+f(x-2)


# print(','.join([str(f(x)) for x in range(0, n+1)]))


# day-16 Q62
# def f(n):
#     if n < 2:
#         fibo[n] = n
#         return fibo[n]
#     fibo[n] = f(n-1) + f(n-2)
#     return fibo[n]


# n = int(input())
# fibo = [0]*(n+1)
# f(n)
# fibo = [str(i) for i in fibo]
# ans = ",".join(fibo)
# print(ans)

# # day-16 Q63
# n = int(input())

# for i in range(0, n+1, 2):
#     if i < n - 1:
#         print(i, end=',')
#     else:
#         print(i)

# day-16 Q64


def generate(n):
    for i in range(n+1):
        if i % 35 == 0:
            yield i


n = int(input())
resp = [str(i) for i in generate(n)]
print(",".join(resp))
