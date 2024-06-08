from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
)
import os
import time
import shutil


def UploadFileEuroMillion():
    def drop_file(filepath):
        try:
            # Vérifier si le fichier existe avant de le supprimer
            if os.path.exists(filepath):
                # Supprimer le fichier
                os.remove(filepath)
                print(f"Le fichier {filepath} a été supprimé avec succès.")
            else:
                print(f"Le fichier {filepath} n'existe pas.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la suppression du fichier : {e}")

    # Effacer les anciens fichiers
    drop_file("GITHUB - EuroMillion/euromillions.csv")
    drop_file("/Users/joeybruno/Downloads/euromillions.csv")

    download_dir = f"/Users/joeybruno/Downloads"

    # Créer la page web automatique sur Safari
    driver = webdriver.Safari()
    driver.get(
        "https://www.loterieplus.com/euromillions/services/telechargement-resultat.php"
    )  # lien de la page web

    try:
        # choix sur séparateur décimale
        select_dec = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sd2"))
        )
        select_dec.click()

        # choix du séparateur de champ
        select_sep = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "sc2"))
        )
        select_sep.click()

        # simulation du click sur le bouton de téléchargement
        valid_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "valid"))
        )
        valid_button.click()

        time.sleep(2)  # délai de téléchargement

        # destination de l'enregistrement du fichier
        destination_file_path = os.path.join(
            f"{os.getcwd()}/GITHUB - EuroMillion/", "euromillions.csv"
        )

        if os.path.exists(f"{download_dir}/euromillions.csv"):
            # Copier le fichier dans le répertoire courant
            shutil.copy(f"{download_dir}/euromillions.csv", destination_file_path)
            print(f"Le fichier a été copié dans {destination_file_path}")
        else:
            print(f"Le fichier euromillions.csv n'existe pas.")

    except TimeoutException:
        print("L'attente de l'élément a dépassé le temps imparti.")
    except NoSuchElementException:
        print("L'élément spécifié est introuvable.")
    except WebDriverException as e:
        print(f"Erreur WebDriver rencontrée: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")
