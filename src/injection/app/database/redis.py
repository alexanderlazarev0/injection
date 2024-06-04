import redis.asyncio as aioredis


_redis = aioredis.from_url(
    f"redis://{CONFIG.redis.address}:{CONFIG.redis.port}",
    username=CONFIG.redis.username.get_secret_value(),
    password=CONFIG.redis.password.get_secret_value(),
    db=CONFIG.redis.db,
    decode_responses=True,
)


async def get_redis() -> aioredis.Redis:
    """
    Get redis instance.
    Returns:
        Redis client.
    """
    return _redis