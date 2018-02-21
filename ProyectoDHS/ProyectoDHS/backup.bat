@echo off
   set BACKUP_FILE=BackupDHS.backup
   echo backup file name is %BACKUP_FILE%
   SET PGPASSWORD=Pa$$w0rd
   echo on
   "C:\Program Files\PostgreSQL\9.4\bin\pg_dump.exe" -h localhost -p 5432 -U postgres -F c -b -v -f "C:\SW3\%BACKUP_FILE%" ProyectoSW3

   