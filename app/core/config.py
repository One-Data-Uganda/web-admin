from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, RedisDsn, validator


class Settings(BaseSettings):
    APPLICATION_NAME: str = "web-admin"
    JAEGER_HOST: str = "jaeger"
    DEPLOYMENT: str = "fdi-sms-gw"

    WEBSOCKET_SSL: Optional[str] = None

    CONFIG_TYPE: str = "prod"
    SECRET_KEY: str = (
        "ife1f905fbf223243cc7d2ec2a3d4a6dd4889d2c5dce51fb9219e9659bbe1becd"
    )
    SESSION_KEY: str = (
        "FBa3kXdBqzbJjkwM2WMYT6vw2qFkLMJcCguCFgpusxNcDuuEwBkbUhjLPU9pCfPj"
    )
    COOKIE_KEY: str = "XrB8wuB7KVs8eP2PEKjfxMU7HtUWZzPkMC8u3kuCMNzrvnxLdpcKuJ6X5z8jHxGX"
    # 60 minutes * 24 hours * 8 days = 8 days
    EXPIRE_HOURS: int = 12
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SENTRY_DSN: Optional[
        HttpUrl
    ] = "https://adcb2a98f729441bbbeeda3cd857af88@sentry.fdibiz.com/3"

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if not v or len(v) == 0:
            return None
        return v

    GRAYLOG_SERVER: str = "178.79.162.225"
    GRAYLOG_PORT: int = 12221

    KYC_FILE_PATH: str = "/data"

    USER_SERVICE: AnyHttpUrl = "http://user-service:5000"
    REPORTING_SERVICE: AnyHttpUrl = "http://reporting-service:5000"
    SMS_SERVICE: AnyHttpUrl = "http://sms-service:5000"
    ACCOUNTING_SERVICE: AnyHttpUrl = "http://accounting-service:5000"
    REPORTING_SERVICE: AnyHttpUrl = "http://reporting-service:5000"

    APIKEY: str = "A8321966-C40F-476D-9038-B6A559D8E0BB"

    NSQD_HOST: str = "nsqd"
    NSQD_PORT: int = 4150

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_TYPE: str = "redis"
    REDIS_URL: Optional[RedisDsn] = None
    CELERY_BACKEND_DB: int = 1
    CELERY_BROKER_DB: int = 0

    CELERY_BACKEND: Optional[RedisDsn] = None
    CELERY_BROKER: Optional[RedisDsn] = None

    @validator("REDIS_URL", pre=True)
    def assemble_redis_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            scheme=values.get("REDIS_TYPE"),
            port=str(values.get("REDIS_PORT")),
            host=values.get("REDIS_HOST"),
        )

    @validator("CELERY_BACKEND", pre=True)
    def assemble_celery_backend(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            scheme=values.get("REDIS_TYPE"),
            port=str(values.get("REDIS_PORT")),
            host=values.get("REDIS_HOST"),
            path=f"/{values.get('CELERY_BACKEND_DB')}",
        )

    @validator("CELERY_BROKER", pre=True)
    def assemble_celery_broker(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn.build(
            scheme=values.get("REDIS_TYPE"),
            port=str(values.get("REDIS_PORT")),
            host=values.get("REDIS_HOST"),
            path=f"/{values.get('CELERY_BROKER_DB')}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
