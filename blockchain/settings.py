from pydantic import BaseSettings, FilePath


class AppSettings(BaseSettings):
    debug: bool = True
    project_name: str = "blockchain"
    api_v1_str: str = "/api/v1"
    log_level: str = 'INFO'


settings = AppSettings()

if settings.debug:
    print('=' * 20)
    for k, v in settings.dict().items():
        print(f'[system-config Config] {k} = {v}')
    print('=' * 20, flush=True)
