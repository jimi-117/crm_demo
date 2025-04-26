FROM python:3.13-slim

WORKDIR /opt/app

COPY . .
RUN pip install .
EXPOSE 8000
CMD ["uvicorn", "src.main:app","--host", "0.0.0.0", "--reload"]