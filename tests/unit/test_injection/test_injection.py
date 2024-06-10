from injection.injector import inject
from injection.provider import Provider, SingletonProvider


def test_demo():
    assert 1 == 1



def test_injection():
    
    
    provider: Provider[_DummyInjectable] = SingletonProvider(_DummyInjectable, 1)
    
    inject(_function_to_wrap)()
    
    
    


class _DummyInjectable:
    
    def __init__(self) -> None:
        pass

def _function_to_wrap(to_inject: _DummyInjectable) -> None:
    pass


class _DummyInjectableClass:
    
    def __init__(self, to_inject: _DummyInjectable) -> None:
        self.injected = to_inject