# specal type of function return values generator functions

def my_generators():
    for i in range(696):
        yield i

gen =my_generators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)