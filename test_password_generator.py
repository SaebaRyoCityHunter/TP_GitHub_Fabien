# Importation de l'environement de test Unittest #
import unittest

# Importation de l'application Password Generator.py et des éléments à tester #
from Password_Generator import generatePassword, replaceWithNumber, replaceWithUppercaseLetter

# Tests à réaliser #
class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self): # vérifie que la longueur du mot de passe généré correspond à la longueur demandée #
        password_lenghts = [7, 13, 22] # test un mdp de longeur 7, 13 et 22 caractères #
        password = generatePassword(password_lenghts) # Définitions des variables #
        for i, password in enumerate(passwords): # Pour chaque génération #
            self.assertEqual(len(password), password_lenghts[i]) # tester les longueurs de caratère prédéfini au dessus #

    def test_password_content(self): # vérifie  la composition des mdp générés #
        password_lenghts = [5, 10, 15] # test un mdp de longeur 5, 10 et 15 caractères #
        passwords = generatePassword(password_lengths) # Définitions des variables #
        self.assertTrue(any(char.isdigit() for char in password)) # vérifie que le mdp généré contient au moins un chiffre (isdigit) #
        self.assertTrue(any(char.isupper() for char in password)) # vérifie que le mdp généré contient au moins une lettre majuscule (isupper) #
        self.assertTrue(any(char.islower() for char in password)) # vérifie que le mdp généré contient au moins une lettre minuscule (islower) #

if __name__ == '__main__': # vérifie si le fichier de test est exécuté en tant que programme principal #
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # ignore le 1er argument pour éviter une erreur + exit=False pour empêcher de quitter le programme après l'exécution des tests #