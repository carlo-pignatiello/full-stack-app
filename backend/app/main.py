from fastapi import FastAPI
from routes import user_router
# import uvicorn

app = FastAPI()

app.include_router(user_router)


# if __name__ == "__main__":
#     uvicorn.run("main:app",host='0.0.0.0', port=4557, reload=True, workers=4)