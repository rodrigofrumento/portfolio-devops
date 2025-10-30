# Project 1 — CI/CD com Docker, Trivy e Deploy em Homolog

Pipeline completo usando GitHub Actions, GHCR e Kubernetes.

## Stack

- FastAPI + Uvicorn
- Pytest
- Docker/Buildx
- Trivy (scan)
- GHCR (registry)
- Kubernetes (Homolog)

## Como rodar local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Pipeline

- Lint & Test → Build → Trivy → Push → Deploy (Homolog)

## Secrets

`KUBECONFIG` (base64), `K8S_NAMESPACE`. Opcional: `GHCR_USERNAME/GHCR_TOKEN`.

## Deploy

Manifests em `k8s/`. Ajuste `image:` para `ghcr.io/OWNER/REPO:latest`.
