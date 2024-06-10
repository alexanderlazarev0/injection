from injection.provider import Provider, SingletonProvider

class _DummyInjectable:
    def __init__(self) -> None:
        pass


def _function_to_wrap(to_inject: _DummyInjectable) -> None:
    pass


class _DummyInjectableClass:
    def __init__(self, to_inject: _DummyInjectable) -> None:
        self.injected = to_inject



def test_provider_returns_correct_class():
    provider: Provider[_DummyInjectable] = SingletonProvider(_DummyInjectable)
    
    assert type(provider.provide()) == _DummyInjectable


def test_singleton_provider_returns_same_instance():
    provider: Provider[_DummyInjectable] = SingletonProvider(_DummyInjectable)
    
    instance1 = provider.provide()
    instance2 = provider.provide()
    
    assert instance1 == instance2
    
def test_singleton_provider_resets_instance():
    provider: Provider[_DummyInjectable] = SingletonProvider(_DummyInjectable)
    
    instance1 = provider.provide()
    provider.reset()
    instance2 = provider.provide()
    
    assert instance1 != instance2


