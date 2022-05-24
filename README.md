# FASTAPI
FASTAPI

```bash
poetry new api-fastapi
poetry add fastapi
poetry add uvicorn
mkdir -p api-fastapi/src/
touch api_fastapi/src/__init__.py
touch api-fastapi/src/main.py
poetry run uvicorn api_fastapi.src.main:app --host 0.0.0.0 --port 80 --reload

```

[FASTAPI docs](http://localhost:80/docs/)