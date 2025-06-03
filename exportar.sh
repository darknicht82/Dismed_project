DB_NAME="sndm1"
DB_USER="postgres"
DB_PASSWORD="root"
BACKUP_FILE="respaldo.sql"

pg_dump -U $DB_USER $DB_NAME > $BACKUP_FILE
gzip $BACKUP_FILE
echo "Exportación completada"
