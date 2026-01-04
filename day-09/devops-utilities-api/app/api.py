from fastapi import FastAPI
from routers import health,logs,aws

app = FastAPI(
    title="Internal health utility app",
    description="This is an internal API app for monitoring health and analyze logs",
    version="1.0.0",
    docs_url="/docs"
)

app.include_router(health.router)
app.include_router(logs.router)
app.include_router(aws.router)