from fastapi import FastAPI

from ksoft.api.routes import router
from ksoft.core.bootstrap import init_db  # Corrected import

app = FastAPI(title="KSoft API")


@app.on_event("startup")
def startup():
    init_db()


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
