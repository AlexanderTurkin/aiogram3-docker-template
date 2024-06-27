FROM python:3.11
LABEL authors="alexturkin"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_HOME="/etc/poetry" \
    POETRY_CACHE_DIR="/tmp/poetry_cache" \
    POETRY_VERSION=1.7.0

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"
RUN poetry install
RUN pip uninstall -y poetry
RUN rm -rf /home/appuser/.cache
RUN rm -rf $POETRY_CACHE_DIR
RUN adduser appuser
RUN chown -R appuser:appuser .

USER appuser

CMD ["python", "-m", "telegram_bot"]