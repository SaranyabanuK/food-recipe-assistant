# Smart Cooking Recipe Assistant

Monorepo scaffold for the Smart Cooking Recipe Assistant system consisting of:

- `frontend/`: Expo (React Native + TypeScript) mobile client starter.
- `backend/`: Django REST API with DRF, CORS support, and OpenAPI schema tooling.

## Prerequisites

- Node.js 20+ (includes `npm`)
- Python 3.12+
- Expo CLI (optional; `npx expo` is used by default)

## Frontend (Expo React Native)

```bash
cd frontend
npm start           # Launch Metro bundler (press `a` for Android emulator, `w` for web, etc.)
```

The template ships with TypeScript support. Add new screens/components under `frontend/app`.

## Backend (Django + DRF)

```bash
cd backend
python -m venv .venv                    # or use any virtual env manager
source .venv/bin/activate
pip install -r requirements.txt         # temporary: pip install django djangorestframework django-cors-headers drf-spectacular
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Key routes:

- `GET /api/health/` ? service health check
- `GET /api/schema/` ? OpenAPI schema
- `GET /api/docs/` ? Interactive Swagger UI

### Virtual Environment (pre-created locally)

A local `.venv` was generated via `virtualenv` and populated with the dependencies above. You may recreate it using the commands in the snippet to ensure consistency on a new machine.

## Next Steps

- Implement domain models (recipes, ingredients, steps, sessions) inside `backend/api`.
- Connect mobile client to backend APIs using an HTTP client (e.g., Axios, React Query).
- Extend Expo app with navigation, onboarding flows, and timer-driven cooking sessions.
- Add comprehensive testing (Jest/Testing Library for frontend, pytest for backend).
