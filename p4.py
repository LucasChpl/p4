import time

def hello():
    return "hello world, it is now " + str(time.ctime())

print(hello())