from dependency_injector import containers, providers

from entities.databases.postgres.database import Database
from entities.databases.postgres.repositories.user_repository import UserRepository
from entities.databases.postgres.services.user_service import UserService


class PostgresContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules = [
            'middlewares.inner.check_auth',
            'routers.user.router',
        ]
    )

    config = providers.Configuration()

    database = providers.Singleton(
        Database,
        host = config.host,
        port = config.port,
        user = config.user,
        password = config.password,
        database = config.database
    )

    user_repository = providers.Factory(
        UserRepository,
        session = database.provided.get_session
    )

    user_service = providers.Factory(
        UserService,
        user_repository = user_repository
    )