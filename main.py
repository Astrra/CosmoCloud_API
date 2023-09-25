from fastapi import FastAPI
from routes.route import router

# Create a FastAPI application instance
app = FastAPI()

# Include the router from the routes.route module
app.include_router(router)
