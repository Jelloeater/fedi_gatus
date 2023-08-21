# fedi_gatus

- Utility program to pull Lemmy data and generate a Gatus YAML file


```mermaid
flowchart
docker_compose 
--creates--> api_server & caddy & config_gen & data_updater

caddy 
--serves--> gatus & api_server 

data_updater
--updated records in --> db

api_server
--queries --> db


config_gen
--pulls data from --> db

config_gen 
--creates config for--> gatus

gatus --store data in--> gatus_postgres
```
