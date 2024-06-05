
from typing import Callable


def inject(func: Callable) -> Callable:
    
    def _wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return _wrapper



