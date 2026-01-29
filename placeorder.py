from dbcon import get_db_connection
from logerror import log_db_error
#========================================================================================
# 2.5 CREATE CUSTOM ORDER
def place_order(product_name, quantity):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT product_id, price, stock FROM products WHERE product_name = %s FOR UPDATE", (product_name,))
        row = cur.fetchone()
        if not row:
            print(f" Product '{product_name}' not found.")
            return
        pid, price, stock = row
        if stock < quantity:
            print(f" Insufficient Stock Requested: {quantity}, Available: {stock}")
            return
        cur.execute("INSERT INTO orders (product_id, quantity) VALUES (%s, %s)", (pid, quantity))
        cur.execute("UPDATE products SET stock = stock - %s WHERE product_id = %s", (quantity, pid))
        conn.commit()
        total = price * quantity
        print(f"Order Placed! Sold {quantity} x {product_name} \n (Total: ${total:.2f})")
    except Exception as e:
        conn.rollback()
        log_db_error(e, "Place Order")
    finally:
        conn.close()
        