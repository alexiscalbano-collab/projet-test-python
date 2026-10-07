import pymysql

from projet_dev_avance.voitures.core.config import DB_CONFIG
from projet_dev_avance.voitures.core.interfaces import Repository
from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable, VoitureDejaPresente
from projet_dev_avance.voitures.models.motorisations import Thermique, Electrique, Hybride
from projet_dev_avance.voitures.models.vehicules.voiture import Voiture

# 2 tables : chaque vehicule pointe vers sa motorisation (motorisation_id)
SELECT_VEHICULES = """
    SELECT v.marque, v.modele, v.annee, v.kilometrage, v.volume_coffre, v.categorie,
           m.type, m.reservoir, m.consommation_thermique, m.batterie, m.consommation_electrique
    FROM vehicules v
    JOIN motorisations m ON m.id = v.motorisation_id
"""


class MariaDBRepository(Repository):

    def __init__(self, config=None):
        self.config = config or DB_CONFIG
        self.creer_tables()

    def _connexion(self):
        return pymysql.connect(**self.config)

    def creer_tables(self):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS motorisations (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        type VARCHAR(20) NOT NULL,
                        reservoir FLOAT,
                        consommation_thermique FLOAT,
                        batterie FLOAT,
                        consommation_electrique FLOAT
                    )
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS vehicules (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        marque VARCHAR(50) NOT NULL,
                        modele VARCHAR(50) NOT NULL UNIQUE,
                        annee INT,
                        kilometrage INT,
                        volume_coffre INT,
                        categorie VARCHAR(30),
                        motorisation_id INT NOT NULL,
                        FOREIGN KEY (motorisation_id) REFERENCES motorisations(id)
                    )
                """)
            conn.commit()
        finally:
            conn.close()

    def ajouter(self, voiture):
        m = voiture.motorisation
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM vehicules WHERE modele = %s", (voiture.modele,))
                if cur.fetchone():
                    raise VoitureDejaPresente("la voiture " + voiture.modele + " existe deja")

                # 1) on enregistre le moteur
                cur.execute(
                    """INSERT INTO motorisations (type, reservoir, consommation_thermique, batterie, consommation_electrique)
                       VALUES (%s, %s, %s, %s, %s)""",
                    (
                        m.type_motorisation,
                        getattr(m, "reservoir", None), getattr(m, "consommation_thermique", None),
                        getattr(m, "batterie", None), getattr(m, "consommation_electrique", None),
                    ),
                )
                motorisation_id = cur.lastrowid

                # 2) on enregistre le vehicule relie a ce moteur
                cur.execute(
                    """INSERT INTO vehicules (marque, modele, annee, kilometrage, volume_coffre, categorie, motorisation_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (
                        voiture.marque, voiture.modele, voiture.annee, voiture.kilometrage,
                        voiture.volume_coffre, voiture.categorie, motorisation_id,
                    ),
                )
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def lister(self):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute(SELECT_VEHICULES)
                lignes = cur.fetchall()
        finally:
            conn.close()
        return [self._vers_voiture(ligne) for ligne in lignes]

    def chercher(self, modele):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute(SELECT_VEHICULES + " WHERE v.modele = %s", (modele,))
                ligne = cur.fetchone()
        finally:
            conn.close()
        if ligne is None:
            raise VoitureIntrouvable("la voiture " + modele + " n'existe pas")
        return self._vers_voiture(ligne)

    def supprimer(self, modele):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT motorisation_id FROM vehicules WHERE modele = %s", (modele,))
                ligne = cur.fetchone()
                if ligne is None:
                    raise VoitureIntrouvable("la voiture " + modele + " n'existe pas")
                # on supprime le vehicule puis son moteur
                cur.execute("DELETE FROM vehicules WHERE modele = %s", (modele,))
                cur.execute("DELETE FROM motorisations WHERE id = %s", (ligne[0],))
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def lister_motorisations(self):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT type, reservoir, consommation_thermique, batterie, consommation_electrique FROM motorisations"
                )
                lignes = cur.fetchall()
        finally:
            conn.close()
        return [self._vers_motorisation(*ligne) for ligne in lignes]

    def vider(self):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM vehicules")
                cur.execute("DELETE FROM motorisations")
            conn.commit()
        finally:
            conn.close()

    def _vers_motorisation(self, type_m, reservoir, conso_th, batterie, conso_el):
        if type_m == "thermique":
            return Thermique(reservoir, conso_th)
        if type_m == "electrique":
            return Electrique(batterie, conso_el)
        return Hybride(reservoir, conso_th, batterie, conso_el)

    def _vers_voiture(self, ligne):
        marque, modele, annee, km, coffre, categorie, *moteur = ligne
        return Voiture(marque, modele, annee, km, self._vers_motorisation(*moteur), coffre, categorie)
