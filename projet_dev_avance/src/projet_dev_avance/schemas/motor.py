from pydantic import BaseModel


class Motor(BaseModel):
    type: str
    reservoir: float | None = None
    consommation_thermique: float | None = None
    batterie: float | None = None
    consommation_electrique: float | None = None
