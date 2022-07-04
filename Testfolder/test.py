import time


def timer(func):
    def wrapper(*args, **kwargs):
        a = time.time()
        func(*args, **kwargs)
        print(f"Time used: {time.time() - a}")
        return func(*args, **kwargs)

    return wrapper


@timer
def return_greeting(name):
    for _ in range(100000):
        pass
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
