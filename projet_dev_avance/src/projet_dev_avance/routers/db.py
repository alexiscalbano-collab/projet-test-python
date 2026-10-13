import pymysql
from fastapi import HTTPException

from projet_dev_avance.voitures.core.config import DB_CONFIG

TABLES = [
    """CREATE TABLE IF NOT EXISTS motorisations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type VARCHAR(20) NOT NULL,
        reservoir FLOAT,
        consommation_thermique FLOAT,
        batterie FLOAT,
        consommation_electrique FLOAT
    )""",
    """CREATE TABLE IF NOT EXISTS vehicules (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(50) NOT NULL,
        modele VARCHAR(50) NOT NULL UNIQUE,
        annee INT,
        kilometrage INT,
        volume_coffre INT,
        categorie VARCHAR(30),
        motorisation_id INT NOT NULL,
        FOREIGN KEY (motorisation_id) REFERENCES motorisations(id)
    )""",
]


def requete(sql, valeurs=()):
    """Lance une requete SQL sur MariaDB et renvoie les lignes."""
    try:
        conn = pymysql.connect(**DB_CONFIG, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as erreur:
        # la base ne tourne pas, ou mauvais port / mot de passe
        raise HTTPException(
            status_code=500, detail="Connexion a MariaDB impossible : " + str(erreur)
        )
    try:
        with conn.cursor() as cur:
            # on cree les tables si elles n'existent pas encore
            for table in TABLES:
                cur.execute(table)
            cur.execute(sql, valeurs)
            lignes = cur.fetchall()
            nouvel_id = cur.lastrowid
            nb = cur.rowcount
        conn.commit()
    finally:
        conn.close()
    return lignes, nouvel_id, nb
