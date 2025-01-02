import os
from functools import wraps
from typing import Optional, Callable, Any


def log(filename: Optional[str]) -> Callable:
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                if os.path.exists(filename):
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                if os.path.exists(filename):
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
        return inner
    return wrapper


@log(filename='mylog.txt')
def my_function(x, y):
    """Функция, которая возвращает сумму аргументов"""
    return x + y


my_function(1, "2")

# Ожидаемый вывод в лог-файл mylog.txt
# при успешном выполнении: my_function ok

# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
