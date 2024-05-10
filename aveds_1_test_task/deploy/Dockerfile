FROM python:3.10-slim-bullseye as base-py-project

ENV WD=/msauth/ \
	POETRY_VERSION=1.3.2 \
	POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

WORKDIR ${WD}

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry==${POETRY_VERSION} && \
	poetry install

COPY . ${WD}

CMD ["poetry", "run", "python", "./aveds_1_test_task/internal/run.py"]

