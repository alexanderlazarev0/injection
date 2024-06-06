from injection.injector import inject
from injection.provider import Provider, SingletonProvider

def _func_with_defaults(a: int, b: int = 1) -> int:
    return a + b

def test_inject_decorator_injects_injected_class():
    inject(_func_with_defaults)(1)