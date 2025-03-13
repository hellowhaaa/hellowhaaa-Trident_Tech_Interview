from fastapi import FastAPI
from src.router import router
app = FastAPI()

app.include_router(router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", port=8000, log_level="info", reload=True, reload_dirs="src")