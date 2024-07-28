





from functools import wraps
from inspect import signature
from pydoc import resolve
from re import T
from typing import Callable, TypeVar

from injection.providers import Provider



T = TypeVar("T")


class Injected:
    """Marker class for injected dependencies."""
    def __init__(self, provider: Provider) -> None:
        self._provider = provider
        
    @property
    def provider(self) -> Provider:
        return self._provider


def inject(func: Callable[..., T]) -> Callable[..., T]:
    """Decorator to inject dependencies into a function.

    Args:
        func (Callable[..., T]): Function to inject dependencies into.

    Returns:
        Callable[..., T]: Decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> T: # type: ignore
        resolved_kwargs = _resolve_args_and_kwargs_to_signature(func, args, kwargs)
        return func(**resolved_kwargs)
    
    return wrapper



def _resolve_args_and_kwargs_to_signature(func: Callable[..., T], args, kwargs) -> dict[str, T]:
    """Resolve the arguments and keyword arguments to the function signature.

    Args:
        func (Callable[..., T]): Function to resolve the arguments and keyword arguments to.
        args: Positional arguments.
        kwargs: Keyword arguments.

    Returns:
        dict[str, T]: Dictionary of resolved arguments and keyword arguments.
    """
    sig = signature(func)
    resolved_args = {}
    for i, (param_name, param) in enumerate(sig.parameters.items()):
        if i < len(args):
            resolved_args[param_name] = args[i]
        elif param_name in kwargs:
            resolved_args[param_name] = kwargs[param_name]
        elif param.default != param.empty:
            if isinstance(param.default, Injected):
                resolved_args[param_name] = param.default.provider.resolve()
    return resolved_args

