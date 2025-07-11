# app/db/init_db.py
import os
import importlib
from app.db.ddbb import Base, engine

def import_models():
    models_dir = os.path.join(os.path.dirname(__file__), "..", "models")
    for filename in os.listdir(models_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.models.{filename[:-3]}"
            importlib.import_module(module_name)

def init_db():
    import_models()
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas")

if __name__ == "__main__":
    init_db()
