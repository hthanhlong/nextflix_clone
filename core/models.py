from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role

class User(models.Model):
    email = models.EmailField(max_length=254, unique=True, db_index=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True, db_index=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    salt = models.CharField(max_length=50, null=False, blank=False, default='hello')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False, blank=False, default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


