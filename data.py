from dbcon import get_db_connection
from logerror import log_db_error
from clean import cleanup_data

def create_tables():
    commands = [
        """CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id SERIAL PRIMARY KEY,
            supplier_name TEXT UNIQUE NOT NULL,
            contact_email TEXT DEFAULT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            product_name TEXT UNIQUE NOT NULL,
            price NUMERIC(10,2) CHECK (price > 0),
            stock INTEGER CHECK (stock >= 0)
        )""",
        """CREATE TABLE IF NOT EXISTS purchases (
            purchase_id SERIAL PRIMARY KEY,
            supplier_id INTEGER REFERENCES suppliers(supplier_id),
            product_id INTEGER REFERENCES products(product_id),
            quantity INTEGER CHECK (quantity > 0),
            purchase_date DATE NOT NULL DEFAULT CURRENT_DATE
        )""",
        """CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES products(product_id),
            quantity INTEGER CHECK (quantity > 0),
            order_date DATE NOT NULL DEFAULT CURRENT_DATE
        )"""
    ]
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        for cmd in commands:
            cur.execute(cmd)
        conn.commit()
    except Exception as e:
        log_db_error(e, "seting up")
    finally:
        conn.close()