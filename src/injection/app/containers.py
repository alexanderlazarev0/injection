



from dependency_injector import containers, providers

from injection.app.database.postgres import PostgresDatabase
from injection.config.schema import Config


class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(modules=["injection.app.endpoints"])
    
    config = providers.Configuration(pydantic_settings=[Config()])
    
    db = providers.Singleton(PostgresDatabase, db_url=f"")