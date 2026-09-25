# AssetLoop

Marketplace for business surplus asset auctions.

## Structure
```
frontend/   Next.js + TypeScript + Tailwind
backend/    Django + DRF, one app per feature area
```

## Local setup
```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
docker compose up
```
Frontend: http://localhost:3000
Backend:  http://localhost:8000/api/

## Branching
- `main` — releases
- `develop` — integration branch
- `feature/AL-XX-short-description`, `fix/AL-XX-short-description`

Jira project key: **AL**
