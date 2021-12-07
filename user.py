class User:

    def __init__(self,number,name,adress=None,email=None,phone=None):
        self.__number = number
        self.__name = name
        self.adress = adress
        self.email=email
        self.phone=phone

    
    @property
    def name(self):
        return self.__name
    
    @property
    def number(self):
        return self.__number

    def change_email(self, new_email):
        """Allow the user to change its email"""
        self.email = new_email
    
    def change_phone(self, new_phone):
        """Allow the User to change its phone"""
        self.phone = new_phone

    def __str__(self):
        return " Number: {}, Name: {}, adress: {}, email: {}, phone: {}"\
                .format(self.__number,self.__name, self.adress, self.email, self.phone)


