from fastapi import FastAPI
from routers import whales, weather  # assuming you still have a weather route
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://127.0.0.1:5500"]  # Add your frontend URL


app = FastAPI(title="Whale Migration API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(whales.router, prefix="/api")
app.include_router(weather.router, prefix="/api")
