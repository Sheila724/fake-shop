import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models.product import Product

load_dotenv()

DB_USER = os.getenv('DB_USER', 'ecommerce')
DB_PASSWORD = os.getenv('DB_PASSWORD', '321FionaStar123')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'ecommerce')

DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    session = SessionLocal()
    produtos = session.query(Product).all()
    session.close()
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

# Exemplo de rota para listar produtos em JSON
@app.get("/produtos")
def listar_produtos():
    session = SessionLocal()
    produtos = session.query(Product).all()
    session.close()
    return [
        {"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos
    ]

# Este arquivo foi migrado para FastAPI, mas agora deve ser removido ou ignorado. Use index.py para rodar o projeto Flask.
