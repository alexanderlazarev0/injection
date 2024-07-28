from inspect import signature
from injection.container import Container
from injection.inject import Injected, inject
from injection.providers import ResourceProvider


def dependency_func() -> int:
    return 42


class MyContainer(Container):
    provider = ResourceProvider[int](func=dependency_func)


@inject
def injected_func(to_inject: int = Injected(MyContainer.provider)) -> int:
    return to_inject


print(signature(injected_func))  # 42
