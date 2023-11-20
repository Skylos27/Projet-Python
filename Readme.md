## Projet

Application de gestion de mots de passes accessible depuis une page web

Les fonctions sont créées avec Python en utilisant le framework Django 
Puis appelée via l'API Django Rest

Création base de donnée : toutes les informations sont stockées en base.
Les mots de passes utilisateurs sont chiffrés à l'aide de clés privées
Les clés privées sont générées de manière asymétrique (seul les utilisateurs ont accès au mot de passe)
## Page de connexion
- S'authentifier (User / Password + mail de confirmation pour 2FA)
	Si l'authentification se fait via une nouvelle IP alors un mail d'information est envoyé au compte
- Créer un compte (User / Password + mail de confirmation de l'email)

## Page d'accueil
- Liste des credentials existants
- Bouton pour ajouter un nouveau credential (User + Password + email + Notes optionnelles)
	  - Lors de l'ajout, un bouton permet de choisir une longueur puis propose un mot de passe sécurisé généré aléatoirement
- Pour chaque credential
	  - Bouton pour le supprimer
	  - Bouton pour éditer les champs
	  - Bouton pour visualiser le mot de passe (Ne plus le masquer sur la page)
	  - Bouton pour partager le mot de passe avec un autre utilisateur de l'application en renseignant son email
	  -  Bouton pour vérifier si ce mot de passe a été leak : en utilisant l'API Have I Been Pwned
# Base de donnée

## User
- UserID (Clé primaire)
- Username
- Password (chiffré)
- Email
- LastLoginIP
- Is2FAEnabled
- 2FASecret (si 2FA est activé)

## Credential
- CredentialID (Clé primaire)
- UserID (Clé étrangère de User)
- Username
- Password (chiffré)
- Email
- Notes (optionnel)

## LoginAttempt
- AttemptID (Clé primaire)
- UserID (Clé étrangère de User)
- AttemptTime
- AttemptIP

## PasswordShare
- ShareID (Clé primaire)
- CredentialID (Clé étrangère de Credential)
- SharedWithUserID (Clé étrangère de User)
- ShareTime

## PasswordLeakCheck
- CheckID (Clé primaire)
- CredentialID (Clé étrangère de Credential)
- CheckTime
- IsLeaked

### Relations

- User a plusieurs Credentials (relation un-à-plusieurs).
- User a plusieurs LoginAttempts (relation un-à-plusieurs).
- Credential peut être partagé avec plusieurs Users via PasswordShare (relation plusieurs-à-plusieurs).
- Credential a plusieurs PasswordLeakChecks (relation un-à-plusieurs).

Ce schéma ORM peut être implémenté en utilisant Django Models
