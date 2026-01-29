import logging
#=================================================================================
# (1.2) FUNCTION TO LOG ERRORS IN LOG FILE AND PRINT 
#
LOG_FILE = "db_errors.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format='%(asctime)s - %(message)s' #DEFINES THE FORMAT OF LOGGIN ERRORS IN THE FILE
)
def log_db_error(error, context): 
    """
    Docstring for log_db_error
    
    Args:-
    - error: feeding in the input error that has occured
    - context: context means which function or which operation failed
    
    will write the error in log file and also print in console for ease of user.
   
    """
    message = f"[{context}] {error}"
    logging.error(message)
    #print(f" Error: {error}")
#=================================================================================