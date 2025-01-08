from fastapi import FastAPI
from routes.root import router as root_router

app = FastAPI()

# Include the router
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)