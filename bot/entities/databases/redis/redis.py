from typing import AsyncIterator

from redis.asyncio import Redis, from_url


async def redis_pool(
    host: str, port: int, db: int
) -> AsyncIterator[Redis]:
    redis = from_url(url = f'redis://{host}:{port}/{db}', encoding="utf-8", decode_responses=True) 
    yield redis
    await redis.close()
    await redis.wait_closed()