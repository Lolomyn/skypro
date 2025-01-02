import os
from functools import wraps
from typing import Any, Callable


def log(filename: str) -> Callable:
    """Декоратор, выводящий логи в консоль или файл о корректном или некорректном исполнении функции"""
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            res = ''
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                if os.path.exists(filename):
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                return res

            else:
                if os.path.exists(filename):
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return res
        return inner

    return wrapper
