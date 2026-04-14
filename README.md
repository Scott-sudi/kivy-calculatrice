# Calculatrice Kivy - APK Android

Ce projet est deja prepare pour generer une application Android installable (.apk).

## Option recommandee (Windows) : build APK via GitHub Actions

Comme Buildozer fonctionne surtout sous Linux, la methode la plus simple depuis Windows est d'utiliser GitHub Actions.

### 1) Envoyer le projet sur GitHub

```powershell
git init
git add .
git commit -m "Setup Android APK build"
git branch -M main
git remote add origin <URL_DE_TON_REPO>
git push -u origin main
```

### 2) Lancer le build

1. Ouvre ton repo sur GitHub.
2. Va dans l'onglet **Actions**.
3. Ouvre le workflow **Build Android APK**.
4. Clique **Run workflow**.

### 3) Recuperer l'APK

1. Quand le job est termine, ouvre l'execution du workflow.
2. Dans **Artifacts**, telecharge `calculatrice-kivy-apk`.
3. Tu recupereras un fichier `.apk`.

### 4) Installer sur ton telephone Android

1. Copie le `.apk` sur ton telephone.
2. Autorise l'installation depuis des sources inconnues (si demande).
3. Ouvre le fichier `.apk` et installe.

## Option locale (Linux / WSL Ubuntu)

Si tu veux builder localement :

```bash
pip install buildozer cython==0.29.36
buildozer android debug
```

L'APK sera genere dans le dossier `bin/`.

## Fichiers importants

- `main.py` : ton application Kivy
- `buildozer.spec` : configuration Android
- `.github/workflows/android-apk.yml` : build automatique APK
- `requirements.txt` : dependances Python
