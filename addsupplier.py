from dbcon import get_db_connection
from logerror import log_db_error
#========================================================================================
# 2.3 ADD SUPPLIER FUNCTION
def add_supplier(name, email):
    sql = "INSERT INTO suppliers (supplier_name, contact_email) VALUES (%s, %s) ON CONFLICT (supplier_name) DO NOTHING"
    conn = get_db_connection()
    try:
        print("entered here")
        cur = conn.cursor()
        cur.execute(sql, (name, email))
        print("check",cur.rowcount)
        conn.commit()
        if cur.rowcount > 0:
            print(f"Supplier '{name}' added successfully.")
        else:
            print(f"\n ! Supplier '{name}' already exists. !")
            print("\n -THIS FEATURE IS ONLY FOR ADDING NEW SUPPLIERS,NOT FOR UPDATING SUPPLIER DETAILS.")
    except Exception as e:
        log_db_error(e, "Add Supplier")
    finally:
        conn.close()