from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from clinic.models import Owner, Pet, MedicalRecord

class Command(BaseCommand):
    help = 'Seeds the database with sample clinic data'

    def handle(self, *args, **options):
        if Pet.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists, skipping seed.'))
            return

        user, _ = User.objects.get_or_create(username='doctor_alex', is_staff=True)
        user.set_password('password123')
        user.save()

        john = Owner.objects.create(user=user, name='John Doe', phone='+123456789')
        mary = Owner.objects.create(user=user, name='Mary Smith', phone='+987654321')

        barsik = Pet.objects.create(owner=john, name='Barsik', species='cat', birth_year=2021)
        rex = Pet.objects.create(owner=mary, name='Rex', species='dog', birth_year=2018)
        charlie = Pet.objects.create(owner=john, name='Charlie', species='dog', birth_year=2023)

        MedicalRecord.objects.create(
            pet=barsik, diagnosis='Routine check-up', treatment='Vaccination shot applied.', cost=1200.00
        )
        MedicalRecord.objects.create(
            pet=rex, diagnosis='Broken paw.', treatment='Applied cast. Prescribed painkillers.', cost=5500.00
        )
        MedicalRecord.objects.create(
            pet=charlie, diagnosis='Allergy reaction', treatment='Changed diet plan. Prescribed antihistamines.', cost=2100.00
        )

        self.stdout.write(self.style.SUCCESS('Database successfully seeded with clinic data.'))