#1 GLOBAL    SCOP
# a=6 #global
# def f1():
#     print(a)
# def f2():
#     global a
#     a+=1
# f1()
from setuptools._distutils.command.py37compat import compose

#1 LOCAL  SCOP
# def f1():
#     a=8 #local
#     print(a)


#3 NONLOCAL SCOP
# def f1():
#     a=4
#     def f2():    #   inner function
#         print(a)   # nonlocal
#     f2()
# f1()


#4
# a=4
# def f1():
#     global a
#     a=5
#     print(a)    # local-->5
# print(a) #  global -->4


#5
# def f1():
#     a=7
#     def f2():   #inner  function
#         nonlocal a
#         a+=2
#     print(a)
# f1()

#6
# def f1():
#     a=4
#     return a
# x=f1()
# f2(f1())


# 7
#
# def f(x):
#     def g(y):
#         return y
#     return g
# a = 5
# b = 1
#
# h=f(a)
# natija = h(b)
# print(natija )  # Output is 1
#
# # yoki
# natija = f(a)(b)
# print(natija )



#8
# def f(x):
#     def g(y):
#         return y
#     return g(y)
#
# a=8
# b=3
# h=f(a)


#9  3  qavatli  funktsiya
# def f(x):
#     def g(y):
#         def  h(z):
#             return z
#         return h
#     return g
# a=5
# b=3
# c=2
# f(a)(b)(c)



#10
# def f(x):
#     z=2
#     def g(y):
#         return z*x+y
#     return g
# a=7
# b=4
# h=f(a)
# print(h(b))



#11
# def f(x):
#     z=2
#     def g(y):
#         return z*x+y
#     return g
# a=8
# b=4
# h=f(a)
# print(h(b))

#12

# print(h.__code__.co_freevars)
# print(h.__closure__[0].sell_contents)
# print(h.__closure__[1].sell_contents)


#13
# def f(x):
#     z=2
#     def g(y):
#         return y
#     return g
# a=11
# b=5
# h=f(a)
# print(h(b))
# print(h.__code__.co_freevars)


#14
# def f(x):
#     def g(y):
#         def h(z):
#             return x*y*z
#         return h
#     return g
# a=12
# b=7
# c=4
# f(a)(b)(c)


#15
# def f(x):
#     z=2
#     return lambda y:z*x+y
# a=6
# b=5
# f(a)(b)
# print(f(a)(b))


#16
# def compose(g,f):
#     def h(*args,**kwargs):
#         return g(f(*args,**kwargs))
#     return h
# compose(5,7)



#17
# km_to_m= lambda x: x*1000
# m_to_sm= lambda x: x * 100
#
# km_to_sm = compose(m_to_sm, km_to_m)
# print(km_to_sm(18))


