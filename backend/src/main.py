from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def read_root():
    return {"message": "Hello, fastapi!"}


if __name__ == "__main__":
    app()
