import flick as f

def slow_func(x): 
    import time
    time.sleep(1)
    print(f'Done! {x}')


def together_example():
    @f.timeit
    def fast():
        f.together(slow_func, ['a','b','c','d'], {})

    @f.timeit
    def slow():
        [slow_func(x) for x in ['a','b','c','d']]

    slow()
    fast()

def json_example():
    a = {"Hello": "world", "Hi": 1+2}
    print(f.json(a))

    a = {"Hello": "א"}
    print(f.json(a))


def s_example():
    a = 123
    print(f.s(a), "Type:", type(f.s(a)))

    a = {"a": 321}
    print(f.s(a), "Type:", type(f.s(a)))

def b_example():
    a = "123"
    print(f.b(a), "Type:", type(f.b(a)))

    a = "א"
    print(f.b(a), "Type:", type(f.b(a)))

def b64_example():
    a = "123"
    print(f.b64(a))

def b64d_example():
    a = "MTIz"
    print(f.b64d(a))

if __name__ == "__main__":
    b64d_example()