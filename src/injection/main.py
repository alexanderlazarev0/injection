from fastapi import FastAPI
from injection.app.endpoints import router as app_router
import uvicorn

app = FastAPI()

app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run("injection.main:app", host="localhost", port=8008, reload=True)