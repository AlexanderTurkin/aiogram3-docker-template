from environs import Env


env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")
BOT_ID: str = BOT_TOKEN.split(":")[0]

LOGGING_LEVEL: int = env.int("LOGGING_LEVEL", 10)

PG_HOST: str = env.str("DB_HOST")
PG_PORT: int = env.int("DB_PORT")
PG_USER: str = env.str("DB_USER")
PG_PASSWORD: str = env.str("DB_PASS")
PG_DATABASE: str = env.str("DB_NAME")

REDIS_HOST: str = env.str("REDIS_HOST")
REDIS_PORT: int = env.int("REDIS_PORT")
REDIS_PASSWORD: str = env.str("REDIS_PASS")

USE_WEBHOOK: bool = env.bool("USE_WEBHOOK", False)

if USE_WEBHOOK:
    MAIN_WEBHOOK_ADDRESS: str = env.str("MAIN_WEBHOOK_ADDRESS")
    MAIN_WEBHOOK_SECRET_TOKEN: str = env.str("MAIN_WEBHOOK_SECRET_TOKEN")

    MAIN_WEBHOOK_LISTENING_HOST: str = env.str("MAIN_WEBHOOK_LISTENING_HOST")
    MAIN_WEBHOOK_LISTENING_PORT: int = env.int("MAIN_WEBHOOK_LISTENING_PORT")

    MAX_UPDATES_IN_QUEUE: int = env.int("MAX_UPDATES_IN_QUEUE", 100)