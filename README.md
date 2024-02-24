# To create database server:
  # Remember to change the left clause of your volume to mount data in another folder. 
  # cd to Resources/Docker and run docker-compose up -d .
  # username: sa; password: 123asd!au.

# To create table in database:
  # Create a Model in folder Model.
  # Modify in DatabaseChangelog.cs (if the table is not declared in this class, it could not be created)
  # dotnet ef migrations add <MigrationName> (for example dotnet ef migrations add Create-Table-Role)
  # dotnet ef database update 