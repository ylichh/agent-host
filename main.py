from fastapi import FastAPI
import uvicorn
import os
app = FastAPI()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-default-key")

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    print("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
