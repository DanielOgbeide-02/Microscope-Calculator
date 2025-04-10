import sqlite3, pathlib
from microscope_calculator import real_size

DB = pathlib.Path("measurements.db")

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS measurements(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            image_size_mm REAL,
            magnification REAL,
            actual_size_um REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")

def save_measurement(user, img_mm, mag):
    act = real_size(img_mm, mag)
    with sqlite3.connect(DB) as conn:
        conn.execute("""INSERT INTO measurements
                        (username, image_size_mm, magnification, actual_size_um)
                        VALUES (?,?,?,?)""",
                     (user, img_mm, mag, act))
    return act

if __name__ == "__main__":
    init_db()
    u  = input("Username: ")
    mm = float(input("Image size (mm): "))
    mag= float(input("Magnification: "))
    actual = save_measurement(u, mm, mag)
    print(f"Saved! Real size ≈ {actual:.2f} µm")
