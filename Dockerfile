FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier tout le projet (y compris manage.py)
COPY . /app/

# Collecte des fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port
EXPOSE 8000

# Commande de lancement
CMD ["gunicorn", "mokinetvet_api.wsgi:application", "--bind", "0.0.0.0:8000"]
