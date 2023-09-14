from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.routes.auth import router as AuthRouter
from app.routes.admin import router as AdminRouter
from app.routes.users import router as UserRouter


app = FastAPI(
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

origins = [
    "http:localhost:8000",
    "http:localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter)
app.include_router(AdminRouter)
app.include_router(UserRouter)


@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Please go to /api/docs endpoint to see API documentation."
    }


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Resto Book",
        description="#Reservation Booking for Restaurant",
        routes=app.routes,
        version="0.0.1",
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi