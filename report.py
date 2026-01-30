from dbcon import get_db_connection
from logerror import log_db_error
#========================================================================================
# 2.6 GEBERATE REPORTS
def generate_reports(report_type):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        if report_type == "daily":
            sql = """SELECT product_name, SUM(o.quantity), SUM(o.quantity * p.price) 
                     FROM orders o JOIN products p ON o.product_id = p.product_id 
                     WHERE o.order_date = CURRENT_DATE GROUP BY product_name"""
            # 3 columns product_name, sum of orders placed,sum of total revenus using both daily orders and price
            # JOINING where product ids match in orders and products table
            # and where the order date is equal to product name
            print("\n--- DAILY SUMMARY ---")
            headers = ["Product", "Sold", "Revenue"]
        else:
            sql = """SELECT supplier_name, COUNT(pu.purchase_id), COALESCE(SUM(pu.quantity),0) 
                     FROM suppliers s LEFT JOIN purchases pu ON s.supplier_id = pu.supplier_id 
                     GROUP BY supplier_name"""
            print("\n---  SUPPLIER SUMMARY ---")
            headers = ["Supplier", "TransActions", "Units Sent"]

        cur.execute(sql)
        #print(sql)
        rows = cur.fetchall()
        print(f"{headers[0]:<20} | {headers[1]:<12} | {headers[2]:<10}")
        print("-" * 50)
        for row in rows:
            val3 = f"${row[2]:.2f}" if report_type == "daily" else str(row[2])
            print(f"{row[0]:<20} | {row[1]:<12} | {val3:<10}")
        print("-" * 50)
    except Exception as e:
        log_db_error(e, "Report Generation")
        print("A server error,please try again!")
    finally:
        conn.close()