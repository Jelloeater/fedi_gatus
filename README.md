# fedi_gatus

- Utility program to pull Lemmy data and generate a Gatus YAML file


```mermaid
flowchart
docker_compose
--> caddy --serves--> gatus & api_server 

api_server --> db
config_gen --server to monitor--> gatus
docker_compose --> config_gen
cron --> updater --> config_gen
```
