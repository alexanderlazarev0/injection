




from abc import ABC, abstractmethod
from typing import Any

from injection.provider import Provider


class Binder(ABC):
    """Describes binding configuration for dependency injection."""


class DeclarativeBinder(Binder):
    pass