from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # store hashed password, not plain text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
