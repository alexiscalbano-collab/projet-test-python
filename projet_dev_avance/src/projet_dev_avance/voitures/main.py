from projet_dev_avance.voitures.repositories import MariaDBRepository
from projet_dev_avance.voitures.services import CatalogueService, MotorisationService, VehiculeService, VoitureFactory
from projet_dev_avance.voitures.cli.menu import lancer_menu


def main():
    repository = MariaDBRepository()

    # injection de dependances : chaque service recoit ce dont il a besoin
    motorisation_service = MotorisationService(repository)
    vehicule_service = VehiculeService(repository)
    service = CatalogueService(vehicule_service, motorisation_service)
    factory = VoitureFactory(motorisation_service)

    # on remplit la base seulement si elle est vide (sinon doublons)
    if not service.lister_voitures():
        service.ajouter_voiture(factory.creer("thermique", "Peugeot", "308", 2019, 45000, 412, "berline", 53, 5.2))
        service.ajouter_voiture(factory.creer("electrique", "Tesla", "Model Y", 2023, 12000, 854, "SUV", 75, 16.9))
        service.ajouter_voiture(factory.creer("hybride", "Toyota", "Corolla", 2021, 30000, 581, "break", 43, 4.5, 1.3, 0.0))

    lancer_menu(service, factory)


if __name__ == "__main__":
    main()
