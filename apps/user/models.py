from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    

    def say_hello(self):
        return "Hello, my name is {}"
    
    
