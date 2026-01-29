from dbcon import get_db_connection
from logerror import log_db_error
#========================================================================================
# 2.7 CLEANUP DATA
def cleanup_data():
   
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM orders WHERE order_date < CURRENT_DATE - INTERVAL '30 days'")
        print(f" Deleted {cur.rowcount} old records.")
        conn.commit()
    except Exception as e:
        log_db_error(e, "Cleanup")
    finally:
        conn.close()
