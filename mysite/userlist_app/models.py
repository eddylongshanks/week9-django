from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=80, null=False)
    secondname = models.CharField(max_length=80, null=False)
    country = models.CharField(max_length=32, null=False)

    # Define __str__ that will be called when querying e.g. 'User.objects.all()'
    def __str__(self):
        obj_str = f'First Name: {self.firstname}, ' \
                  f'Second Name: {self.secondname}, ' \
                  f'Country: {self.country}' \

        return obj_str

class ChatMessage(models.Model):
    author = models.CharField(max_length=80, null=False)
    message = models.CharField(max_length=400, null=False)

    def __str__(self):
        obj_str = f'Message: {self.message}, ' \
                  f'Author: {self.author}, ' \
    
        return obj_str
