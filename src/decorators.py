def log(filename):
    def wrapper(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            print(res)
            return res

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл mylog.txt
# при успешном выполнении: my_function ok

# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
