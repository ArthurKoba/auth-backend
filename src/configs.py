from sqlalchemy.engine.url import URL


DB_DRIVER = "postgresql+asyncpg"
DB_HOST = "localhost"
DB_PORT = 5432
DB_DATABASE = "auth-backend"
DB_USER = "auth-backend-user"
DB_PASSWORD = "password"

DB_ECHO = False
DB_POOL_SIZE = 5
DB_MAX_OVERFLOW = 0


DB_DSN = URL.create(
    DB_DRIVER,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
)
