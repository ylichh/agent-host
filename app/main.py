from fastapi import FastAPI
import uvicorn
import os
app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

def create_app():

    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"message": "Hello, FastAPI!"}
    return app





if __name__ == "__main__":
    print("Starting FastAPI server...")
    app = create_app()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
