# MokineVet
# MokineVetBackend

Backend de l'application **MokineVet** — une plateforme de gestion vétérinaire complète pour les éleveurs, vétérinaires et administrateurs.

## 📦 Technologies utilisées

- Python 3.10+
- Django 5.2+
- Django REST Framework
- Simple JWT (authentification)
- MySQL (base de données)

## 🚀 Installation et configuration

### 1. Cloner le projet

```bash
git clone https://github.com/TRU237/MokineVetBackend.git
cd MokineVetBackend
python -m venv env
source env/bin/activate  # (Linux/macOS)
env\Scripts\activate     # (Windows)
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
