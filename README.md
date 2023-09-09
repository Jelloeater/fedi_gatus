# fedi_gatus
[![Test](https://github.com/Jelloeater/fedi_gatus/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/Jelloeater/fedi_gatus/actions/workflows/test.yml)
[![CodeQL](https://github.com/Jelloeater/fedi_gatus/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Jelloeater/fedi_gatus/actions/workflows/codeql.yml)
[![GitHub](https://img.shields.io/github/license/Jelloeater/fedi_gatus)](https://github.com/Jelloeater/fedi_gatus/blob/main/LICENSE)


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

# Usage
- Install gotask
- Fill out .env.example and rename to .env
- task run

# Cloud Deploy
- See cloud-init.yaml.example for userdata deploy
