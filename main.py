from fastapi import FastAPI
from routes.routes import router as person_router
from config.database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routes
app.include_router(person_router, tags=["CRUD Operations in MYSQL"])

@app.get("/")
async def root():
    return {"message": "MySQL with FASTAPI is running!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
