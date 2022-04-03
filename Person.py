class Person:
     def __init__(self, firstname, lastname, phonenumber):
         self.firstname = firstname
         self.lastname = lastname
         self.phonenumber = phonenumber

     def get_full_name(self):
         return self.firstname + ' ' + self.lastname
        
     def get_phonenumber(self):
         return self.phonenumber

     @classmethod
     def get_user_input(self):
        while 1:
            firstname = input('Enter first name: ')
            lastname = input('Enter last name: ')
            phonenumber = input('Enter phonenumber: ')
            return self(firstname, lastname, phonenumber)
            

personA = Person.get_user_input()
nameA = personA.get_full_name()
phoneNumberA = personA.get_phonenumber()
personB = Person.get_user_input()
nameB = personB.get_full_name()
phoneNumberB =personB.get_phonenumber()


print('fullNameLengthA > fullNameLengthB', nameA > nameB)
print('phoneNumberA - phoneNumberB', int(phoneNumberA) - int(phoneNumberB))
