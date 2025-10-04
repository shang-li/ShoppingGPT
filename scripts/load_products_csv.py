import os
import csv
import sqlite3
from typing import Sequence

DEFAULT_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "products.db")


def load_csv(csv_path: str, db_path: str = DEFAULT_DB_PATH) -> int:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(csv_path)
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows: Sequence[tuple] = [
                (
                    r.get('product_code'),
                    r.get('product_name'),
                    r.get('material'),
                    r.get('size'),
                    r.get('color'),
                    r.get('brand'),
                    r.get('gender'),
                    int(r.get('stock_quantity') or 0),
                    float(r.get('price') or 0.0),
                )
                for r in reader
            ]
        cur.executemany(
            """
            INSERT OR REPLACE INTO products
            (product_code, product_name, material, size, color, brand, gender, stock_quantity, price)
            VALUES (?,?,?,?,?,?,?,?,?)
            """,
            rows,
        )
        conn.commit()
        return len(rows)
    finally:
        conn.close()


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Load products from CSV into SQLite DB")
    p.add_argument("csv", help="Path to CSV with products")
    p.add_argument("--db", default=DEFAULT_DB_PATH, help="Path to SQLite DB (defaults to data/products.db)")
    args = p.parse_args()
    count = load_csv(args.csv, args.db)
    print(f"Loaded {count} rows into {os.path.abspath(args.db)}")

