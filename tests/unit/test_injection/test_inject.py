






import pytest
from injection.container import Container
from injection.inject import inject, Injected
from injection.providers import ResourceProvider

@pytest.fixture
def _create_container() -> Container: 
    
    def _dependency_func() -> int:
        return 42
    
    class _Container(Container):
        provider = ResourceProvider[int](func=_dependency_func)
        
        
    return _Container()


def test_inject_with_single_injection(_create_container: Container) -> None:
    
    @inject
    def _injected_func(to_inject: int = Injected(_create_container.provider) ) -> int:
        return to_inject
    
    assert _injected_func() == 42, "Dependency should be injected correctly."
    assert _injected_func(41) == 41, "Dependency should be override correctly by arg."
    assert _injected_func(to_inject=41) == 41, "Dependency should be override correctly by kwarg."
    
    
    
    
def test_inject_with_override(_create_container: Container) -> None:
    
    def _override_func() -> int:
        return 43
    
    @inject
    def _injected_func(to_inject: int = Injected(_create_container.provider) ) -> int:
        return to_inject
    
    with _create_container.provider.override(_override_func):
        assert _injected_func() == 43
        
    assert _injected_func() == 42, "Dependency should be injected correctly."
    


def test_inject_with_multiple_injections(_create_container: Container) -> None:
    
    def _dependency_func_2() -> int:
        return 43
    
    class _Container(Container):
        provider_2 = ResourceProvider[int](func=_dependency_func_2)
        
    @inject
    def _injected_func(to_inject: int = Injected(_create_container.provider),
                       to_inject_2: int = Injected(_Container.provider_2)) -> int:
        return to_inject + to_inject_2
    
    assert _injected_func() == 85, "Dependencies should be injected correctly."
    assert _injected_func(1) == 44, "Dependency should be override correctly by arg."
    assert _injected_func(to_inject=1) == 44, "Dependency should be override correctly by kwarg."
    assert _injected_func(1, 1) == 2, "Dependency should be override correctly by args."
    assert _injected_func(1, to_inject_2=1) == 2, "Dependency should be override correctly by args and kwargs."
    
    
def test_inject_with_multiple_injections_and_override(_create_container: Container) -> None:
    
    def _dependency_func_2() -> int:
        return 43
    
    class _Container(Container):
        provider_2 = ResourceProvider[int](func=_dependency_func_2)
        
    @inject
    def _injected_func(to_inject: int = Injected(_create_container.provider),
                       to_inject_2: int = Injected(_Container.provider_2)) -> int:
        return to_inject + to_inject_2
    
    def _override_func() -> int:
        return 44
    
    with _Container.provider_2.override(_override_func):
        assert _injected_func() == 86
        
    assert _injected_func() == 85
    
    
def test_inject_with_single_injection_and_args(_create_container: Container) -> None:
    
    @inject
    def _injected_func(a: int, to_inject: int = Injected(_create_container.provider),
                       ) -> int:
        return to_inject + a
    
    assert _injected_func(1) == 43, "Dependency should be injected correctly."
    # should throw an error because the function is missing a required argument
    with pytest.raises(TypeError):
        _injected_func()
    
def test_inject_with_single_injection_and_kwargs(_create_container: Container) -> None:
    
    @inject
    def _injected_func(a: int, to_inject: int = Injected(_create_container.provider),
                       ) -> int:
        return to_inject + a
    
    assert _injected_func(a=1) == 43
    
    
def test_inject_with_single_injection_and_args_and_kwargs(_create_container: Container) -> None:
    
    @inject
    def _injected_func(a: int, b: int, to_inject: int = Injected(_create_container.provider),
                       ) -> int:
        return to_inject + a + b
    
    assert _injected_func(1, b=2) == 45
    
def test_inject_with_nested_injections(_create_container: Container) -> None:
    
    def _dependency_func_2() -> int:
        return 43
    
    class _Container(Container):
        provider_2 = ResourceProvider[int](func=_dependency_func_2)
        
    @inject
    def _injected_func(to_inject: int = Injected(_create_container.provider),
                       to_inject_2: int = Injected(_Container.provider_2)) -> int:
        return to_inject + to_inject_2
    
    @inject
    def _injected_func_2(to_inject: int = Injected(_create_container.provider),
                       to_inject_2: int = Injected(_Container.provider_2),
                       to_inject_3: int = Injected(_create_container.provider)) -> int:
        return to_inject + to_inject_2 + to_inject_3
    
    assert _injected_func() == 85, "Dependencies should be injected correctly."
    assert _injected_func_2() == 127, "Dependencies should be injected correctly."
    
    
    
    
