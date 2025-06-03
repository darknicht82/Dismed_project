import subprocess
import logging
import os
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from dotenv import load_dotenv
from datetime import datetime

logger = logging.getLogger(__name__)


def load_env_and_configure():
    # Cargar variables de entorno desde el archivo .env en dismed_project
    env_path = os.path.join(settings.BASE_DIR, "./dismed_project/.env")
    load_dotenv(dotenv_path=env_path)
    db_user = os.getenv("DB_USER")
    db_name = os.getenv("DB_NAME")
    db_password = os.getenv("DB_PASSWORD")
    env = os.environ.copy()
    env["PGPASSWORD"] = str(db_password)

    if db_user is None or db_name is None or db_password is None:
        raise Exception("Error al cargar las variables de entorno.")

    return db_user, db_name, db_password, env


@user_passes_test(lambda u: u.is_superuser)
def crear_backup(request):
    backup_folder_path = os.path.join(settings.BASE_DIR, "backup_manager/backups")
    backup_files = [f for f in os.listdir(backup_folder_path) if f.endswith(".snmd1")]

    if request.method == "POST":
        try:
            db_user, db_name, _, env = load_env_and_configure()
            os.makedirs(backup_folder_path, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            backup_file_name = f"backup_{timestamp}.snmd1"
            backup_file_path = os.path.join(backup_folder_path, backup_file_name)
            command = [
                "pg_dump",
                "-U",
                db_user,
                "-F",
                "c",
                "-b",
                "-v",
                "-f",
                backup_file_path,
                db_name,
            ]
            subprocess.run(command, check=True, stderr=subprocess.PIPE, env=env)
            messages.success(
                request, f"El backup: {backup_file_name}, ha sido creado exitosamente"
            )
            return redirect("crear_backup")
        except Exception as e:
            logger.error(str(e))
            return HttpResponse(f"Error al crear el backup: {str(e)}", status=500)

    else:
        return render(request, "backup.html", {"backup_files": backup_files})


@user_passes_test(lambda u: u.is_superuser)
def import_backup(request, backup_file):
    backup_folder_path = os.path.join(settings.BASE_DIR, "backup_manager/backups")
    try:
        db_user, db_name, _, env = load_env_and_configure()
        backup_path = os.path.join(backup_folder_path, f"{backup_file}.snmd1")
        command = [
            "pg_restore",
            "-U",
            db_user,
            "-d",
            db_name,
            "--clean",
            "--if-exists",
            "--verbose",
            backup_path,
        ]
        subprocess.run(command, check=True, stderr=subprocess.PIPE, env=env)
        messages.success(request, f"El backup {backup_file} fue importado exitosamente")
        return redirect("crear_backup")
    except Exception as e:
        logger.error(str(e))
        return HttpResponse(f"Error al importar el backup: {str(e)}", status=500)
