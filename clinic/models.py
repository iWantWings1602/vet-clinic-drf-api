from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='clinic_owners',
                             null=True,
                             blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Pet(models.Model):
    owner = models.ForeignKey(Owner,
                              on_delete=models.CASCADE,
                              related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    birth_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.species})"


class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet,
                            on_delete=models.CASCADE,
                            related_name='records')
    diagnosis = models.CharField(max_length=255)
    treatment = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Record for {self.pet.name} from {self.date_created}"