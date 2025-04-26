FROM python:3.13-slim

WORKDIR /opt/app

COPY pyproject.toml .
COPY src/ ./src/

RUN pip install .
COPY . .
EXPOSE 8000
CMD ["uvicorn", "src.main:app","--host", "0.0.0.0", "--reload"]