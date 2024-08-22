from dependency_injector import containers, providers

from entities.databases.redis.redis import redis_pool
from entities.databases.redis.services.service import Service


class UserRedisContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules = [
            'middlewares.inner.check_auth',
            'routers.user.router',
        ]
    )

    config = providers.Configuration()

    redis_pool = providers.Resource(
        redis_pool,
        host = config.host,
        port = config.port,
        db = config.db,
    )

    redis_service = providers.Factory(
        Service,
        redis = redis_pool
    )


class TasksRedisContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules = [
            'middlewares.inner.check_auth',
            'routers.user.router',
        ]
    )

    config = providers.Configuration()

    redis_pool = providers.Resource(
        redis_pool,
        host = config.host,
        port = config.port,
        db = config.db,
    )

    redis_service = providers.Factory(
        Service,
        redis = redis_pool
    )
