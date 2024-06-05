

from abc import ABC, abstractmethod
from typing import override


class Provider[T](ABC):
    
    
    def __init__(self, cls: T, *args, **kwargs) -> None:
        self._cls = cls
        self._args = args
        self._kwargs = kwargs
        
        
    @abstractmethod
    def provide(self) -> T:
        """Provide an instance of the type for injection.

        Returns:
            T: instance.
        """
    
    
    
    
class SingletonProvider[T](Provider[T]):
    """Provides a singleton instance of a type."""
    
    
    
    def __init__(self, cls: T, *args, **kwargs) -> None:
        super().__init__(cls, *args, **kwargs)
        self._instance = None
        self._is_reset = True
    
    
    def reset(self) -> None:
        """Reset the singleton instance."""
        self.is_reset = True
        self._instance = None
        
    @override
    def provide(self) -> T:
        if self.is_reset:
            self._instance = self._cls(*self._args, **self._kwargs)
            self.is_reset = False
        return self._instance
    
    
class TransientProvider[T](Provider[T]):
    """Provides a new instance of a type each time."""
    
    @override
    def provide(self) -> T:
        return self._cls(*self._args, **self._kwargs)
    