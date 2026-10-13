from pydantic import BaseModel


class Car(BaseModel):
    marque: str
    modele: str
    annee: int
    kilometrage: int
    volume_coffre: int
    categorie: str
    motorisation_id: int
