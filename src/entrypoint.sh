#!/bin/bash
set -e  # Para encerrar imediatamente se algum comando falhar

# Exporta o nome da aplicação Flask
export FLASK_APP=index.py

if [ "$1" = "migrate" ]; then
  echo "Executando flask db upgrade..."
  flask db upgrade
elif [ "$1" = "run" ]; then
  echo "Iniciando Gunicorn..."
  gunicorn --bind 0.0.0.0:8217 index:app
else
  echo "Comando não reconhecido. Use 'migrate' ou 'run'."
  exec "$@"
fi


