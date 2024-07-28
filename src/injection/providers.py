"""Providers for dependency injection."""
from abc import ABC, abstractmethod
import contextlib
from typing import Callable, Generator


class Provider[T](ABC):
    def __init__(self, func: Callable[..., T]) -> None:
        super().__init__()
        self._func = func

    @abstractmethod
    def resolve(self) -> T:
        """Resolve the dependency.

        Returns:
            T: Resolved dependency.
        """

    @contextlib.contextmanager
    def override(self, func: Callable[..., T]) -> Generator[None, None, None]:
        """Temporarily override the provider's function.

        Args:
            func (Callable[..., T]): New function to use.

        Yields:
            Generator[None, None, None]: Context manager.
        """
        old_func = self._func
        self._func = func
        try:
            yield
        finally:
            self._func = old_func


class ResourceProvider[T](Provider[T]):
    def resolve(self) -> T:
        return self._func()


class SingletonProvider[T](Provider[T]):
    def __init__(self, func: Callable[..., T]) -> None:
        super().__init__(func)
        self._value = None

    def resolve(self) -> T:
        if self._value is None:
            self._value = self._func()
        return self._value

    @contextlib.contextmanager
    def override(self, func: Callable[..., T]) -> Generator[None, None, None]:
        old_func = self._func
        self._func = func
        old_value = self._value
        self._value = None
        try:
            yield
        finally:
            self._func = old_func
            self._value = old_value
