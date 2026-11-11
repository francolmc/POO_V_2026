import sqlite3
from pathlib import Path

RUTA_BD = Path(__file__).resolve().parent.parent / "juego_rol.db"

def obtener_conexion():
    return sqlite3.connect(RUTA_BD)

def crear_tablas(conexion: sqlite3.Connection):
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS personajes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL,
        nivel INTEGER NOT NULL,
        vida INTEGER NOT NULL CHECK (vida BETWEEN 0 AND 100),
        poder INTEGER NOT NULL
    )
    """)
    conexion.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS idx_nombre ON personajes(nombre)
    """)