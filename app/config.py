from functools import lru_cache
from pydantic import BaseSettings


class AppSettings(BaseSettings):
    app_name: str
    admin_email: str
    app_dir: str
    app_host: str
    app_port: int
    app_reload: bool
    api_prefix: str
    docs_prefix: str

    class Config:
        env_file = ".env"


class DBSettings(BaseSettings):
    mysql_db_url: str
    db_name: str
    
    class Config:
        env_file = ".env"


class AuthSettings(BaseSettings):
    jwt_secret: str
    jwt_algorithm: str
    jwt_expiry_time: int  # seconds

    class Config:
        env_file = ".env"


class LogSettings(BaseSettings):
    """One-time setup for logging"""

    log_base_dirs: str
    log_backup_count: int
    log_date_format: str
    log_app_file_name: str
    log_audit_file_name: str
    log_error_file_name: str
    log_users_file_name: str
    log_format: str
    log_interval: int
    log_level: str
    log_style: str
    log_when: str

    class Config:
        env_file = ".env"


# SETTING FUNCTIONS
# We are using the @lru_cache() decorator on top of each function
# the settings object will be created only once, the first time it's called.
@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache()
def get_db_settings() -> DBSettings:
    return DBSettings()


@lru_cache
def get_auth_settings() -> AuthSettings:
    return AuthSettings()


# ADDITIONAL FUNCTIONS
def setup_log_settings():
    """One-time setup for logging"""

    import logging.config
    import os

    cfg = LogSettings()

    # Create logs folder if it doesn't exist.
    if not os.path.isdir(os.path.join(cfg.log_base_dirs)):
        os.makedirs(os.path.join(cfg.log_base_dirs))

    timed_rotating_file_handler_cfg = {
        "level": cfg.log_level,
        "class": "logging.handlers.TimedRotatingFileHandler",
        "when": cfg.log_when,
        "interval": cfg.log_interval,
        "backupCount": cfg.log_backup_count,
    }

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": cfg.log_format,
                "style": cfg.log_style,
                "datefmt": cfg.log_date_format,
            }
        },
        "handlers": {
            "app_handler": {  # app log handler
                "filename": os.path.join(cfg.log_base_dirs, cfg.log_app_file_name),
                "formatter": "standard",
                **timed_rotating_file_handler_cfg,
            },
            "audit_handler": {  # audit log handler
                "filename": os.path.join(cfg.log_base_dirs, cfg.log_audit_file_name),
                **timed_rotating_file_handler_cfg,
            },
            "error_handler": {  # error log handler
                "filename": os.path.join(cfg.log_base_dirs, cfg.log_error_file_name),
                "formatter": "standard",
                **timed_rotating_file_handler_cfg,
            },
            "users_handler": {  # consumers log handler
                "filename": os.path.join(cfg.log_base_dirs, cfg.log_users_file_name),
                "formatter": "standard",
                **timed_rotating_file_handler_cfg,
            },
        },
        "loggers": {
            "": {
                "handlers": ["app_handler"],
                "level": cfg.log_level,
                "propagate": True,
            },
            "audit": {
                "handlers": ["audit_handler"],
                "level": cfg.log_level,
                "propagate": True,
            },
            "error": {
                "handlers": ["error_handler"],
                "level": cfg.log_level,
                "propagate": True,
            },
            "users": {
                "handlers": ["users_handler"],
                "level": cfg.log_level,
                "propagate": True,
            },
        },
    }