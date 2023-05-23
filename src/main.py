import uvicorn
from fastapi import FastAPI
from src.routers import helloworld

app = FastAPI(title="testing api", version="0.1.0")
app.include_router(helloworld.router)


# @app.on_event("startup")
# def on_startup() -> None:



if __name__ == "__main__":
    uvicorn.run(app, reload=True)
