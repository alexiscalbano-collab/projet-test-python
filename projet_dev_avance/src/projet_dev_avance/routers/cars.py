from fastapi import APIRouter, HTTPException
from pymysql.err import IntegrityError

from projet_dev_avance.routers.db import requete
from projet_dev_avance.schemas.car import Car

router = APIRouter(prefix="/cars", tags=["cars"])


def valeurs(car):
    return (
        car.marque,
        car.modele,
        car.annee,
        car.kilometrage,
        car.volume_coffre,
        car.categorie,
        car.motorisation_id,
    )


@router.get("/")
async def get_cars():
    lignes, _, _ = requete("SELECT * FROM vehicules")
    return lignes


@router.post("/")
async def create_car(car: Car):
    try:
        _, car_id, _ = requete(
            "INSERT INTO vehicules (marque, modele, annee, kilometrage, "
            "volume_coffre, categorie, motorisation_id) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            valeurs(car),
        )
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Modele deja present ou moteur inexistant"
        )
    return {"id": car_id, **car.model_dump()}


@router.get("/{car_id}")
async def get_car(car_id: int):
    lignes, _, _ = requete("SELECT * FROM vehicules WHERE id = %s", (car_id,))
    if not lignes:
        raise HTTPException(status_code=404, detail="Voiture introuvable")
    return lignes[0]


@router.put("/{car_id}")
async def update_car(car_id: int, car: Car):
    await get_car(car_id)
    try:
        requete(
            "UPDATE vehicules SET marque = %s, modele = %s, annee = %s, "
            "kilometrage = %s, volume_coffre = %s, categorie = %s, "
            "motorisation_id = %s WHERE id = %s",
            valeurs(car) + (car_id,),
        )
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Modele deja present ou moteur inexistant"
        )
    return {"id": car_id, **car.model_dump()}


@router.delete("/{car_id}")
async def delete_car(car_id: int):
    _, _, nb = requete("DELETE FROM vehicules WHERE id = %s", (car_id,))
    if nb == 0:
        raise HTTPException(status_code=404, detail="Voiture introuvable")
    return {"message": "Voiture supprimee"}


# bonus : le moteur d'une voiture
@router.get("/{car_id}/motors")
async def get_car_motor(car_id: int):
    car = await get_car(car_id)
    lignes, _, _ = requete(
        "SELECT * FROM motorisations WHERE id = %s", (car["motorisation_id"],)
    )
    return lignes[0]
