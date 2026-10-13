from fastapi import APIRouter, HTTPException
from pymysql.err import IntegrityError

from projet_dev_avance.routers.db import requete
from projet_dev_avance.schemas.motor import Motor

router = APIRouter(prefix="/motors", tags=["motors"])

COLONNES = "type, reservoir, consommation_thermique, batterie, consommation_electrique"


def valeurs(motor):
    return (
        motor.type,
        motor.reservoir,
        motor.consommation_thermique,
        motor.batterie,
        motor.consommation_electrique,
    )


@router.get("/")
async def get_motors():
    lignes, _, _ = requete("SELECT * FROM motorisations")
    return lignes


@router.post("/")
async def create_motor(motor: Motor):
    _, motor_id, _ = requete(
        f"INSERT INTO motorisations ({COLONNES}) VALUES (%s, %s, %s, %s, %s)",
        valeurs(motor),
    )
    return {"id": motor_id, **motor.model_dump()}


@router.get("/{motor_id}")
async def get_motor(motor_id: int):
    lignes, _, _ = requete("SELECT * FROM motorisations WHERE id = %s", (motor_id,))
    if not lignes:
        raise HTTPException(status_code=404, detail="Moteur introuvable")
    return lignes[0]


@router.put("/{motor_id}")
async def update_motor(motor_id: int, motor: Motor):
    await get_motor(motor_id)
    requete(
        "UPDATE motorisations SET type = %s, reservoir = %s, "
        "consommation_thermique = %s, batterie = %s, "
        "consommation_electrique = %s WHERE id = %s",
        valeurs(motor) + (motor_id,),
    )
    return {"id": motor_id, **motor.model_dump()}


@router.delete("/{motor_id}")
async def delete_motor(motor_id: int):
    try:
        _, _, nb = requete("DELETE FROM motorisations WHERE id = %s", (motor_id,))
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Moteur utilise par une voiture")
    if nb == 0:
        raise HTTPException(status_code=404, detail="Moteur introuvable")
    return {"message": "Moteur supprime"}
