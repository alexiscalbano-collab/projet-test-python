import os

# config de la base MariaDB (lancee avec docker sur le port 3307)
# on peut changer les valeurs avec des variables d'environnement sans toucher au code
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", "3307")),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "root"),
    "database": os.environ.get("DB_NAME", "garage"),
}
