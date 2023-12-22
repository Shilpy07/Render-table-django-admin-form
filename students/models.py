from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Student Details"

    def __str__(self):
        return f"{self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return f"{self.name}"
