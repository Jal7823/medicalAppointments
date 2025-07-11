# 🩺 apiSpecialties

Microservicio de especialidades médicas para el sistema de gestión de citas médicas.

---

## 🚀 Tecnologías

- Python 3.11
- FastAPI
- SQLite
- SQLAlchemy
- Alembic
- Pytest + Allure (para testing)

---

## 📦 Instalación local

```bash
git clone https://github.com/tu-usuario/medicalAppointments.git
cd apiSpecialties
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Accede a la API en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker

```bash
docker build -t api-specialties .
docker run -d -p 8000:8000 --name api-specialties-container api-specialties
```

---

## 🧪 Ejecutar Tests

```bash
pytest
```

Con reportes Allure:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📂 Alembic (Migraciones)

```bash
alembic revision --autogenerate -m "mensaje"
alembic upgrade head
```

---

## 🔗 Endpoints Principales

| Método | Endpoint             | Descripción              |
|--------|----------------------|--------------------------|
| GET    | /specialties/        | Lista todas las activas |
| POST   | /specialties/        | Crea una nueva          |
| GET    | /specialties/{id}    | Detalle por ID          |
| PUT    | /specialties/{id}    | Reemplaza por ID        |
| PATCH  | /specialties/{id}    | Modifica por ID         |
| DELETE | /specialties/{id}    | Desactiva por ID        |
