"""Point d'entrée de l'application de gestion des véhicules."""
import uvicorn
from fastapi import FastAPI
from projet_dev_avance.routers import cars, motors


def main():
    app = FastAPI()
    app.include_router(cars.router, prefix="/api")
    app.include_router(motors.router, prefix="/api")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
