from django.db import models

# Create your models here.

class User (models.Model):
    user_email = models.EmailField ()
    user_password = models.CharField (max_length=20)
    name = models.CharField (max_length=40)
    age = models.IntegerField ()
    weight = models.IntegerField ()
    doctor = models.CharField (max_length=10, null=True)
    emergency = models.CharField (max_length=10, null=True)

    def __str__(self):
        return self.name



class Reminder (models.Model):
    person = models.ForeignKey (User, default=1, on_delete=models.CASCADE)
    remind_date = models.DateTimeField()
    reminder_description = models.CharField (max_length=40, default='Add a reminder')

    def __str__(self):
        return self.reminder_description [:20]

    class Meta:
        ordering = ['remind_date']