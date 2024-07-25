class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        lcase = False
        for i in password:
            if i.islower():
                lcase = True
        if lcase == False:
            return False
        
        ucase = False
        for i in password:
            if i.isupper():
                ucase = True
        if ucase == False:
            return False
        
        dig = False
        for i in password:
            if i.isdigit():
                dig = True
        if dig == False:
            return False
        
        spl = False
        for i in password:
            if i in "!@#$%^&*()-+":
                spl = True
        if spl == False:
            return False
        
        temp = ""
        for i in password:
            if i == temp:
                return False
            else:
                temp = i
        
        return True