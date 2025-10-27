class Validator(object):
  
    def pw_validator(self, password):
        min_len = 8
        max_len = 15
        valid_chars = {'-','_','.','!','@','#','$','^','&','(',')'}
    
        if len(password) >= min_len and len(password) <= max_len:
            if any(char in password for char in valid_chars):
                if any(char.isdigit() for char in password):
                    if any(char.isupper() for char in password):
                        if any(char.islower() for char in password):
                            return True
         
        return False  


