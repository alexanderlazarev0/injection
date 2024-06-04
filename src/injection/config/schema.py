


from typing import Final
from pathlib import Path
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, YamlConfigSettingsSource

_CONFIG_LOADER_YAML_PATH: Final[Path] = Path("config_settings.yaml")

class Settings(BaseSettings):
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            YamlConfigSettingsSource(settings_cls=settings_cls),
            file_secret_settings,
            dotenv_settings,
        )
        
        
class ConfigLoader(BaseSettings):
    """Configuration for loading configuration."""

    model_config = SettingsConfigDict(
        env_prefix="CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        yaml_file=_CONFIG_LOADER_YAML_PATH,
    )
    data_path: Path = Path(".data")
    config_yaml_filename: str = "config.yaml"
    config_uvicorn_log_filename: str = "log_conf.yaml"

    def config_yaml_path(self) -> Path:
        """
        Path to general configuration file.
        Returns: path.

        """
        return self.data_path / self.config_yaml_filename

    def config_uvicorn_log_path(self) -> Path:
        """
        Path to uvicorn logging configuration file.
        Returns: path.

        """
        return self.data_path / self.config_uvicorn_log_filename
    
# Load configuration file settings.
_CONFIG_SETTINGS: Final = ConfigLoader()


class ConfigPostgresSql(BaseModel):
    """Configuration for PostgreSQL database."""

    host: str
    port: int
    database: str
    user: SecretStr
    password: SecretStr

class ConfigRedis(BaseModel):
    """Configuration for Redis database."""

    host: str
    port: int
    db: int

class Config(Settings):
    """Configuration for the backend application."""

    model_config = SettingsConfigDict(
        env_prefix="BACKEND__",
        env_nested_delimiter="__",
        case_sensitive=False,
        yaml_file=_CONFIG_SETTINGS.config_yaml_path(),
    )
    postgres: ConfigPostgresSql
    redis: ConfigRedis
    
    
    