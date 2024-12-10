#DECORATOR


# def query(f):
#     def g(*args, **kwargs):
#         print(f"Funksiya chaqirildi: {f.__name__}")
#         return f(*args, **kwargs)
#     return g
#
# @query
# def func(x):
#     return 2 * x
#
# result = func(5)
# print(result)



# def deco(f):
#     def g(*args, **kwargs):
#         print("by Asliddin ", f.__name__)
#         return f(*args, **kwargs)
#     return g
#
# def func(x):
#     return 2*x
#
# func = deco(func)
# func(2)


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(6):
#     print(fib(i), end=" ")



# def memoize(f):
#     memo = {}
#     def memoized_func(n):
#         if n not in memo:
#             memo[n] = f(n)
#         return memo[n]
#     return memoized_func


#1-masala..FUNKSIYA  QAYTARADIGAN  VA STRINGNI  KATTA HARFGA  O'TKAZADIGAN DEKORATOR YARATING :
# def katta_harfga(func):
#     def wrapper(*args,**kwargs):
#         result=func(*args,**kwargs)
#         return result.upper()
#     return wrapper
# @katta_harfga
# def greet(name):
#     return f"Hello {name}!"
# result=greet("Asliddin")
# print(result)



#2-MASALA...
# def to_reverse(func):
#     def orash(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return ''.join(reversed(result))
#         return result
#     return orash
# @to_reverse
# def greet(name):
#     return f"Salom, {name}!"
# print(greet("Asliddin aka"))



#3-MISOL..
# import time
#
# def timer_dekorator(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         result=func(*args,**kwargs)
#         end_time=time.time()
#         print(f"{func.__name__ } took {end_time-start_time:.2f}s  vaqt  o'tdi")
#     return wrapper
# @timer_dekorator
# def timer():
#     a=0
#     for i in range(999999):
#
#         a+=5
# timer()

#4-MISOL..FUNKSIYA  NECHA   MARTA   CHAQIRILGANINI  SANOVCHI  DEKORATOR   YARATING
# def chaqiruv_sanovchi(func):
#     func.call_count = 0
#
#     def wrapper(*args, **kwargs):
#         func.call_count += 1
#         result = func(*args, **kwargs)
#         print(f"Funksiya {func.__name__} {func.call_count} marta chaqirildi.")
#         return result
#
#     return wrapper
#
# @chaqiruv_sanovchi
# def sample_function(n):
#     return sum(range(n))
#
# print(sample_function(20))
# print(sample_function(25))
# print(sample_function(45))





