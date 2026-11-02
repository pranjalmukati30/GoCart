from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    app_name : str
    app_version : str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Setting()