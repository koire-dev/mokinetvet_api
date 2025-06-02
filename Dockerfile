# Image officielle python 3.11 slim
FROM python:3.11-slim

# Variables d'environnement pour éviter la mise en buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installer les dépendances système nécessaires (gcc, etc.)
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copier requirements.txt et installer les dépendances Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier tout le code source
COPY . /app/

# Exposer le port 8000
EXPOSE 8000

# Commande par défaut pour lancer le serveur Django en mode production (modifie selon besoin)
CMD ["gunicorn", "mokinetvet_api.wsgi:application", "--bind", "0.0.0.0:8000"]
