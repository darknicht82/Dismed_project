#!/bin/bash

PATH="/c/Program Files/PostgreSQL/12/bin:$PATH"
DB_NAME="dismed"
DB_USER="postgres"
BACKUP_FILE="respaldo.sql.gz"

# Descomprimir el archivo de respaldo
gunzip $BACKUP_FILE

# Crear la nueva base de datos
createdb -U $DB_USER $DB_NAME

# Importar el archivo de respaldo en la nueva base de datos
psql -U $DB_USER $DB_NAME < respaldo.sql

echo "Importación completada"
