import sys, json
from typing import Optional, Tuple
from session_lambda import session, set_session_data, get_session_data, init_session_store

@session(update=True)
def lambda_handler(event, context):
    # get session data out of dynamodb table, if it exists
    session_data = get_session_data() or {}
    
    # get client input data
    message = event["body"]
    
    # put client's message into session data
    set_session_data(message)
            
    return {
        "statusCode": 200, 
        "headers":{"Content-Type":"application/json"}
    }