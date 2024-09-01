from django.db import models

# Create your models here.\
class Project(models.Model):
    id= models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    def __str__(self):
        return self.project_name
    
class Client(models.Model):
    id= models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='clients',  null=True, blank=True)
    created_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client_name
    
class User(models.Model):
    id= models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='users', null=True, blank=True)
    
    def __str__(self):
        return self.user_name
    
