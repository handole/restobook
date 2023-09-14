import uvicorn

from app import app_settings

if __name__ == "__main__":
    uvicorn.run(
        app=app_settings.app_dir,
        host=app_settings.app_host,
        port=app_settings.app_port,
        reload=app_settings.app_reload,
    )