from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from item.item_router import router as item_router

from database import item_Base, item_engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

item_Base.metadata.create_all(bind=item_engine)

app.include_router(item_router, tags=["item"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)