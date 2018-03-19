@echo off
echo ---------------------------------------------------------------------------------//
echo Bienevnido a la aplicacion DHS
echo ---------------------------------------------------------------------------------//
echo Generando Backup
echo ---------------------------------------------------------------------------------//
echo Por favor no cierre esta ventana hasta terminar de usar la aplicacion
"C:\SW3\DonDanielProject\ProyectoDHS\ProyectoDHS\backup.vbs"
echo ---------------------------------------------------------------------------------//
echo on
"C:\SW3\DonDanielProject\ProyectoDHS\manage.py" runserver
