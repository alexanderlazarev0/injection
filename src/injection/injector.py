from functools import wraps
from typing import Callable


def inject(func: Callable) -> Callable:
    
    @wraps(func)
    def _wrapper(*args, **kwargs):
        print(f"{func.__kwdefaults__}")
        return func(*args, **kwargs)

    return _wrapper
