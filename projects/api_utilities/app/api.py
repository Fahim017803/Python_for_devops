from fastapi import FastAPI
from routers import metrics
from routers import aws

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="Internal API for system metrics and AWS utilities",
    version="1.1.0",
    docs_url="/docs",
)


@app.get("/")
def hello_friend():
    return {"message": "Hello my friend"}


app.include_router(metrics.router)
app.include_router(aws.router)
