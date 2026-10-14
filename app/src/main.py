from fastapi import FastAPI

app = FastAPI(
    title="Uptime Monitoring Platform",
    description="Self-hosted website monitoring service",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "Uptime Monitoring Platform",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
