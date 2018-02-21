@echo off
    set BACKUP_FILE=BackupDHS.backup
    echo backup restore file name is %BACKUP_FILE%
    SET PGPASSWORD=Pa$$w0rd
    echo on
    "C:/Program Files/PostgreSQL/9.4/bin\pg_restore.exe" --host localhost --port 5432 --username "postgres" --dbname "ProyectoSW3" --verbose "C:\SW3\BackupDHS.backup"