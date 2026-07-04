# 2 type of type casthing
'''
1::Explicit Type Casting

a="1"
print(int(a))

2::Implicit Type Casting
a=2
b=2.2
print(a+b)
'''

# 4 type of argument

'''
i) defualt argument : a=10
ii) reqired argument : 
iii) keyword argument : does not mater order
iv) variable length arument : * use (tuple)
'''

# doc string

# def seq(n):
#     ''' n sequare is : n'''
#     return n*n

# print(seq(5))
# print(seq.__doc__)
# ------------------------------------------------------------------------------------------------------------
# pep 8

# zen of pyton print

# import this
# ----------------------------------------------------------------------------------------------------------
# recursion

# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         return n * fact(n-1)
    
# n=7
# print("Factorial:",fact(n))
# -----------------------------fibonacci------------------------------------
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return fibo(n - 1) + fibo(n - 2)

# terms = 1

# print(f"Fibonacci series up to {terms} terms:")

# for i in range(terms):
#     print(fibo(i), end=" ")
