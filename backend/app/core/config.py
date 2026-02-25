from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Verified SocialMedia API"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    # CORS — allow the Next.js frontend origin
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
