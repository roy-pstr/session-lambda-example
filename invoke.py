import sys, json
from typing import Optional, Tuple
from lambda_function import lambda_handler

def parse_args() -> Tuple[Optional[str], Optional[str]]:
    message = None
    session_id = None
    if len(sys.argv) == 1:
        raise ValueError("message is required")
    if len(sys.argv) > 1:
        message = sys.argv[1]
    if len(sys.argv) > 2:
        message = sys.argv[2]
        session_id = sys.argv[1]
    return message, session_id

if __name__ == "__main__":
    message, session_id = parse_args()
    response = lambda_handler({"body": message, "headers": {"session-id": session_id}},{})
    print(json.dumps(response))