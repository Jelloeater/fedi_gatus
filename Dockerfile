FROM python:3.10-slim AS base

# Setup env
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PYTHONUNBUFFERED=1

#FROM base AS python-deps
WORKDIR /app

# Set timezone
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install python dependencies
RUN apt-get update && apt-get install -y --no-install-recommends tree libpq-dev #gcc git
# Setup Poetry
RUN pip install poetry
# Skip venvs for Docker
RUN poetry config virtualenvs.create false

# Install application into container
# Don't forget to check the .dockerignore
COPY pyproject.toml .
COPY poetry.lock .
# Install ALL packages
RUN poetry install --no-interaction --no-root --without test
COPY . .
RUN tree /app
#RUN pip install -e .
# TODO Switch this to run as user,
# Create and switch to a new user
#RUN useradd --create-home appuser
#RUN chown appuser:appuser -R /app/
#USER appuser
#RUN chmod a+rwx -R /app/
ENV PYTHONPATH "${PYTHONPATH}:/fedi_gatus"
