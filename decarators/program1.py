def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner

@make_pretty
def ordenery():
    print("i am ordenery")
ordenery()


def make_pretty(func):
    def inner():
        print("i got decorated")
    return inner

def ordenery():
    print("i am ordenery")
result=make_pretty(ordenery())
result()