from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class Program(models.Model):
    title = models.CharField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    university = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.University", related_name="university_program_s")
    tuition_fee = models.DecimalField(blank=False, null=False, max_digits=11, decimal_places=2)
    duration = models.CharField(blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    website = models.URLField(blank=True, null=True)
    category = models.ForeignKey(blank=True, null=True, on_delete=models.CASCADE, to="mainapp.Category", related_name="category_program_s")
    country = models.CharField(blank=True, null=True)
    language = models.CharField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)

class University(models.Model):
    name = models.CharField(blank=False, null=False)
    logo = models.ImageField(blank=True, null=True, upload_to="logo_images/")
    contact_email = models.EmailField(blank=False, null=False)
    def __str__(self):
        return str(self.name)

class Category(models.Model):
    name = models.CharField(blank=False, null=False, unique=True)
    def __str__(self):
        return str(self.name)

class ProgramApplication(models.Model):
    program = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Program", related_name="program_programapplication_s")
    name = models.CharField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    location = models.CharField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.name)

class ProgramSubmission(models.Model):
    program = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Program", related_name="program_programsubmission_s")
    is_pinned = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    payment = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Payment", related_name="payment_programsubmission_s")
    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    amount = models.DecimalField(blank=False, null=False, max_digits=11, decimal_places=2)
    payment_date = models.DateTimeField(blank=False, null=False)
    stripe_charge_id = models.CharField(blank=False, null=False)
    def __str__(self):
        return str(self.id)
