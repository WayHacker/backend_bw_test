import re
def validate_pin(pin):
    if re.match(r"---insert your code---", pin) is None :
        return False
    return True
