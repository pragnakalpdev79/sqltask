from dbcon import get_db_connection
from logerror import log_db_error
from validate import get_valid_input
#========================================================================================
# 2.2 UPSERT (UPDATE OR INSERT) PRODUCT FUNCTION 
def upsert_product(name, price):
    """
    Docstring for upsert_product
    - queries the database to look for matching name
    - if there are no mathes this will be empty hence we will need to insert because the product does not exist
    Args:     
    - name: str
    - price: float
    """
    conn = get_db_connection()

    try:
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM products WHERE product_name = %s", (name,)) 
        if cur.fetchone(): 
            cur.execute("UPDATE products SET price = %s WHERE product_name = %s", (price, name))
            print(f" Product '{name}' updated with new price: ${price}.")
            #now asking the user if they want to update the stock or not
            cur.execute("SELECT stock FROM products WHERE product_name= %s \n ",(name,))
            existing_stock = cur.fetchone()
            print(f"Current stock is {existing_stock[0]} \n")
            print("Do you Want to update the existing stock for the product?")
            checkif = input("ENTER Y to update stock , or preess any other key to continue").strip().lower()
            if checkif == 'y':
                stock = get_valid_input("ENTER THE STOCK TO BE ADDED",int) 
                cur.execute("UPDATE products SET stock = %s WHERE product_name = %s", (stock, name))
                print("Stock Updated!!")     
        else:
            stock = get_valid_input("ENTER THE INTIAL STOCK",int) 
            cur.execute("INSERT INTO products (product_name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
            print(f" New product '{name}' created.")
        conn.commit()
    except Exception as e:
        log_db_error(e, "Upsert Product")
    finally:
        conn.close()