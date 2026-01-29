from dbcon import get_db_connection
from logerror import log_db_error
#========================================================================================
# 2.4 RECORD PURCHASE
def record_purchase(supplier, product, quantity):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT supplier_id FROM suppliers WHERE supplier_name = %s", (supplier,))
        s_row = cur.fetchone()
        cur.execute("SELECT product_id FROM products WHERE product_name = %s", (product,))
        p_row = cur.fetchone()
        if not s_row or not p_row:
            print(" Invalid Supplier or Product name.")
            return
        cur.execute("INSERT INTO purchases (supplier_id, product_id, quantity) VALUES (%s, %s, %s)", 
                    (s_row[0], p_row[0], quantity))
        cur.execute("UPDATE products SET stock = stock + %s WHERE product_id = %s", (quantity, p_row[0]))
        conn.commit()
        print(f" Restocked {quantity} units of {product}.") 
    except Exception as e:
        conn.rollback()
        log_db_error(e, "Record Purchase")
    finally:
        conn.close()