@echo off
for /f "tokens=1-4 delims=/ " %%i in ("%date%") do (
     set dow=%%i
     set month=%%j
     set day=%%k
     set year=%%l
   )
   set datestr=%month%_%day%_%year%
   echo datestr is %datestr%
    
   set BACKUP_FILE=BackupDHS_%datestr%.backup
   echo backup file name is %BACKUP_FILE%
   SET PGPASSWORD=Pa$$w0rd
   echo on
   "C:\Program Files\PostgreSQL\9.4\bin\pg_dump.exe" -h localhost -p 5432 -U postgres -F c -b -v -f "C:\SW3\%BACKUP_FILE%" ProyectoSw3   