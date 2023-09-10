
n.n.n / 2023-09-10
==================



v1.0.2 / 2023-09-10
===================

  * fix: DB sort query
  * version bump

v1.0.1 / 2023-09-09
===================

  * fix: Fixed test suite for missing env var
  * doc: Updated changelog and readme

v1.0.0 / 2023-09-09
===================

  * doc: Update readme
  * feat: Added number of servers to env var
  * doc: Added prod deploy note
  * feat: Added order by for top instances
  * doc: readme update
  * Added example Cloud init

v0.1.0 / 2023-09-09
===================

  * Updated build
  * Added changelog
  * feat: Added poetry build option
  * Update README.md
  * dev: Removed ARM build... timeing out
  * fix: GH Actions plus Dockerfile user fix
  * Finished updating template
  * Added additional links
  * Swapped to root user... meh
  * Added missing chmod to file dir in Dockerfile
  * wip: Working, but need to chmod 777 config dir
  * doc: Added note on adding API endpoint link to gatus link bar
  * fix: Fixed docker build order
  * fix: Fixed config gen write permissions and DB updater
  * Added logging
  * Added API link
  * dev: updated build order
  * Updated dependcies
  * doc: updated diagram
  * fix: Added drop before insert, for refreshing data
  * doc: Adde notes
  * doc: Added DB create note
  * Need to have domain, or when version changes they'll get a new entry, it will break badges
  * fix: Fixed URL path and server desc
  * wip: Config pull and gen is working, need to fix YAML syntax
  * fix: You need to either create a DB first or use the default 'postgres' one... FUN! -_-
  * fix: Fixed select query
  * feat: fixed updaterq
  * dev: Added image build
  * dev: temp disable security
  * wip: Need to debug update function
  * wip: Started on update function
  * wip: Added postgres driver to build, still need to finish updater
  * Fixed to instance query
  * doc: Added todo for PD alerting
  * wip: started on data query
  * Fixed import ^_^
  * Added data mapping
  * wip: Refactoring data insert into class method
  * feat: Added better API endpoint check
  * doc: Added todo
  * wip: need to add new model
  * dev: Added missing .env examples
  * dev: Adde missing unit tests
  * wip: ... it works?!?? Adding stuff to db in test moduele
  * wip: working, but need to clean up data model
  * fix: Refactored DB connection to only create live connection when called, NOT when module is loaded https://stackoverflow.com/questions/44984429/how-to-manage-a-peewee-database-in-a-separate-module
  * test: Updated test suite
  * fix: Fixed API server path
  * Added template to security ignore
  * FIX: Working api server now w/ un-versioned endpoint
  * wip: Swagger API broken now :-(
  * wip: Gatus working, need to fix api
  * wip: update ports
  * wip: Need to fix API router for docs
  * Added HTTP for local testing
  * Swapped DB config to Postgres
  * Template refactor
  * working w/ SQL lite
  * Minor cleanup
  * wip: Just need to get endpoint to generate properly, so close!
  * doc: Added TODOq
  * Fixed imports, needed to add env var back to docker file
  * Fixed updater as well
  * fix: FIXED BAD FastAPI version pin FML
  * broken build
  * wip: Docker build broken
  * wip: File logging working, need to fix path next
  * dev: Refactored classes for clarity
  * wip: need to figure out log levels
  * dev: Fixed class structure and unit tests
  * wip: module refactor
  * doc: Started on dependency graph
  * wip: Started on seperate docker workers
  * wip: Started on AIO repo
  * doc: Added todo note
  * wip: Started on DB for storage
  * wip: Started on REST API pull
  * wip: Started on REST API pull
  * wip: Finished config gen
  * Added UI template generator
  * Added yaml var gen
  * wip: App starts
  * Initial Commit
