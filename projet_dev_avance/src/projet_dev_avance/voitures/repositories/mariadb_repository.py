import pymysql

from projet_dev_avance.voitures.core.interfaces import Repository
from projet_dev_avance.voitures.core.exceptions import VoitureIntrouvable, VoitureDejaPresente
from projet_dev_avance.voitures.models.motorisations import Thermique, Electrique, Hybride
from projet_dev_avance.voitures.models.vehicules.voiture import Voiture

COLONNES = """marque, modele, annee, kilometrage, volume_coffre, categorie,
    type_motorisation, reservoir, consommation_thermique, batterie, consommation_electrique"""


class MariaDBRepository(Repository):

    def __init__(self, host="localhost", port=3306, user="root", password="root", database="garage"):
        self.config = dict(host=host, port=port, user=user, password=password, database=database)
        self.creer_table()

    def _connexion(self):
        return pymysql.connect(**self.config)

    def _executer(self, requete, params=None):
        conn = self._connexion()
        try:
            with conn.cursor() as cur:
                cur.execute(requete, params)
                lignes = cur.fetchall()
            conn.commit()
            return lignes
        finally:
            conn.close()

    def creer_table(self):
        self._executer("""
            CREATE TABLE IF NOT EXISTS voitures (
                id INT AUTO_INCREMENT PRIMARY KEY,
                marque VARCHAR(50) NOT NULL,
                modele VARCHAR(50) NOT NULL,
                annee INT,
                kilometrage INT,
                volume_coffre INT,
                categorie VARCHAR(30),
                type_motorisation VARCHAR(20) NOT NULL,
                reservoir FLOAT,
                consommation_thermique FLOAT,
                batterie FLOAT,
                consommation_electrique FLOAT
            )
        """)

    def ajouter(self, voiture):
        if self._executer("SELECT id FROM voitures WHERE modele = %s", (voiture.modele,)):
            raise VoitureDejaPresente("la voiture " + voiture.modele + " existe deja")

        m = voiture.motorisation
        self._executer(
            f"INSERT INTO voitures ({COLONNES}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                voiture.marque, voiture.modele, voiture.annee, voiture.kilometrage,
                voiture.volume_coffre, voiture.categorie, m.type_motorisation,
                getattr(m, "reservoir", None), getattr(m, "consommation_thermique", None),
                getattr(m, "batterie", None), getattr(m, "consommation_electrique", None),
            ),
        )

    def lister(self):
        lignes = self._executer(f"SELECT {COLONNES} FROM voitures")
        return [self._vers_voiture(ligne) for ligne in lignes]

    def chercher(self, modele):
        lignes = self._executer(f"SELECT {COLONNES} FROM voitures WHERE modele = %s", (modele,))
        if not lignes:
            raise VoitureIntrouvable("la voiture " + modele + " n'existe pas")
        return self._vers_voiture(lignes[0])

    def supprimer(self, modele):
        self.chercher(modele)  # leve VoitureIntrouvable si elle existe pas
        self._executer("DELETE FROM voitures WHERE modele = %s", (modele,))

    def vider(self):
        self._executer("DELETE FROM voitures")

    def _vers_voiture(self, ligne):
        marque, modele, annee, km, coffre, categorie, type_m, reservoir, conso_th, batterie, conso_el = ligne

        if type_m == "thermique":
            moteur = Thermique(reservoir, conso_th)
        elif type_m == "electrique":
            moteur = Electrique(batterie, conso_el)
        else:
            moteur = Hybride(reservoir, conso_th, batterie, conso_el)

        return Voiture(marque, modele, annee, km, moteur, coffre, categorie)
