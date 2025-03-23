from django.contrib import admin
from mainapp.models import *

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'country', 'language', 'is_featured', 'is_pinned', 'is_published']
    search_fields = ['title', 'description', 'duration', 'country', 'language']

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(ProgramApplication)
class ProgramApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location', 'message']

@admin.register(ProgramSubmission)
class ProgramSubmissionAdmin(admin.ModelAdmin):
    list_display = ['is_pinned', 'is_featured']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['stripe_charge_id']
    search_fields = ['stripe_charge_id']
