# re = lista[::-1]
# re1 = sorted(lista, reverse=True)
# ling = [{'br': 'port'}, {'eua': 'ing'}]
# a = ling[0].values()
# args1 = (2, 1, 98)
# kwargs1 = {'nome': 'Igor', 'idade': 16}
# def soma(*args, **kwargs):
#     print(args)
#     print(kwargs)

# soma(*args1, **kwargs1)
# n = 2000
# n1 = 0
# n2 = 2000000
# a = 0.15
# a1 = 0
# while True:
#     n += 1000
#     n2 -= n
#     n1 += 1
#     if n > n2:
#         print(n1)
#         break
# while True:
#     a += 0.05
#     a1 += 1
#     if a1 == 60:
#         print(a)
lst = [2, 4, 6, 8, 10]
mt = list(map(lambda n: n / 2, lst))
lst2 = ['A', 'B', 'C', 'D', 'E']
dc = {i:lst2[i] for i in range(len(lst2))}
print(dc)