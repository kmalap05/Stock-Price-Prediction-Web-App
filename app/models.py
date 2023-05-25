from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)  # Field to store the name of the project
    start_date = models.DateField()  # Field to store the start date of the project
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)  # Field to store the responsible user for the project
    week_number = models.CharField(max_length=2, blank=True)  # Field to store the week number of the project (optional)
    end_date = models.DateField()  # Field to store the end date of the project

    def __str__(self):
        return str(self.name)  # String representation of the project object (returns the project name)

    def save(self, *args, **kwargs):
        # Calculate the week number based on the start date if it is not provided
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args, **kwargs)  # Call the save method of the superclass (Model) to save the project object
