import os
from functools import wraps
from typing import Callable, Any


def log(filename: str) -> Callable:
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                func(*args, **kwargs)
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
