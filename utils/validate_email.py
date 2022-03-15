import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
    
class Validate_email():
    def isvalidEmail(email):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.match(pattern,email):
            return True
