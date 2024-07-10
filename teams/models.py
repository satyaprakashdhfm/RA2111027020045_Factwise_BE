from django.db import models
from users.models import user

# Create your models here.

class team(models.Model):
    teamname = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    creationtime = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(user, related_name='admin', on_delete=models.CASCADE, to_field="id")
    members = models.ManyToManyField(user,max_length=50,help_text='Select members for this team')

    def __str__(self) -> str:
        return self.teamname
    
    def display_members(self):
        return ', '.join(members.name for members in self.members.all()[:])

    display_members.short_description = 'Users'