from fastapi import FastAPI

#routes
from app.routes.routeSpecialties import router as specialtiesRoutes

app = FastAPI()
app.include_router(specialtiesRoutes,prefix='/api')

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
