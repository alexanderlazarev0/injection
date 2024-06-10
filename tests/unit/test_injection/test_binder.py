

from re import L

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from injection.binder import DeclarativeBinder
from injection.provider import SingletonProvider

class _Settings(BaseSettings):
    pass

class _DummyConfig(BaseModel):
    dummy_variable: str
class _DummySettings(_Settings):
    dummy_config: _DummyConfig

class _DummyService:
    
    def __init__(self, dummy_config: _DummyConfig) -> None:
        self.dummy_variable = dummy_config.dummy_variable

class _DummyBinder(DeclarativeBinder):
    
    config = _DummySettings(dummy_config=_DummyConfig(dummy_variable="dummy"))
    
    dummy_service = SingletonProvider(_DummyService, config.dummy_config)
    


def test_binder():
    
    assert isinstance(_DummyBinder().dummy_service.provide(), _DummyService)