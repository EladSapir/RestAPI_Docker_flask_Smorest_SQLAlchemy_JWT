# CONTRIBUTING

## HOW TO RUN THE DOCKER FILE LOCALLY

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
"flask run"
```