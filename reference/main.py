from fastapi import FastAPI

mw = FastAPI()

hello = "there"

@mw.get("/api")
def get_root():
    return "Hello there!"