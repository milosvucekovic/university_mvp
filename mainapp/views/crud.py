from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.models import *
from django import forms

class ProgramListView(ListView):
    model = Program
    template_name = 'mainapp/program_list.html'
    context_object_name = 'program_list'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'mainapp/program_detail.html'
    context_object_name = 'program'

class ProgramCreateView(CreateView):
    model = Program
    fields = ['title', 'description', 'university', 'tuition_fee', 'duration', 'start_date', 'website', 'category', 'country', 'language', 'is_featured', 'is_pinned', 'is_published']

    template_name = 'mainapp/program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = ['title', 'description', 'university', 'tuition_fee', 'duration', 'start_date', 'website', 'category', 'country', 'language', 'is_featured', 'is_pinned', 'is_published']

    template_name = 'mainapp/program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'mainapp/program_confirm_delete.html'
    success_url = reverse_lazy('program_list')

class UniversityListView(ListView):
    model = University
    template_name = 'mainapp/university_list.html'
    context_object_name = 'university_list'

class UniversityDetailView(DetailView):
    model = University
    template_name = 'mainapp/university_detail.html'
    context_object_name = 'university'

class UniversityCreateView(CreateView):
    model = University
    fields = ['name', 'logo', 'contact_email']

    template_name = 'mainapp/university_form.html'
    success_url = reverse_lazy('university_list')

class UniversityUpdateView(UpdateView):
    model = University
    fields = ['name', 'logo', 'contact_email']

    template_name = 'mainapp/university_form.html'
    success_url = reverse_lazy('university_list')

class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'mainapp/university_confirm_delete.html'
    success_url = reverse_lazy('university_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'mainapp/category_list.html'
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'mainapp/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    template_name = 'mainapp/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    template_name = 'mainapp/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'mainapp/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class ProgramApplicationListView(ListView):
    model = ProgramApplication
    template_name = 'mainapp/programapplication_list.html'
    context_object_name = 'programapplication_list'

class ProgramApplicationDetailView(DetailView):
    model = ProgramApplication
    template_name = 'mainapp/programapplication_detail.html'
    context_object_name = 'programapplication'

class ProgramApplicationCreateView(CreateView):
    model = ProgramApplication
    fields = ['program', 'name', 'email', 'location', 'message']

    template_name = 'mainapp/programapplication_form.html'
    success_url = reverse_lazy('programapplication_list')

class ProgramApplicationUpdateView(UpdateView):
    model = ProgramApplication
    fields = ['program', 'name', 'email', 'location', 'message']

    template_name = 'mainapp/programapplication_form.html'
    success_url = reverse_lazy('programapplication_list')

class ProgramApplicationDeleteView(DeleteView):
    model = ProgramApplication
    template_name = 'mainapp/programapplication_confirm_delete.html'
    success_url = reverse_lazy('programapplication_list')

class ProgramSubmissionListView(ListView):
    model = ProgramSubmission
    template_name = 'mainapp/programsubmission_list.html'
    context_object_name = 'programsubmission_list'

class ProgramSubmissionDetailView(DetailView):
    model = ProgramSubmission
    template_name = 'mainapp/programsubmission_detail.html'
    context_object_name = 'programsubmission'

class ProgramSubmissionCreateView(CreateView):
    model = ProgramSubmission
    fields = ['program', 'is_pinned', 'is_featured', 'payment']

    template_name = 'mainapp/programsubmission_form.html'
    success_url = reverse_lazy('programsubmission_list')

class ProgramSubmissionUpdateView(UpdateView):
    model = ProgramSubmission
    fields = ['program', 'is_pinned', 'is_featured', 'payment']

    template_name = 'mainapp/programsubmission_form.html'
    success_url = reverse_lazy('programsubmission_list')

class ProgramSubmissionDeleteView(DeleteView):
    model = ProgramSubmission
    template_name = 'mainapp/programsubmission_confirm_delete.html'
    success_url = reverse_lazy('programsubmission_list')

class PaymentListView(ListView):
    model = Payment
    template_name = 'mainapp/payment_list.html'
    context_object_name = 'payment_list'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'mainapp/payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['amount', 'payment_date', 'stripe_charge_id']

    template_name = 'mainapp/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['amount', 'payment_date', 'stripe_charge_id']

    template_name = 'mainapp/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'mainapp/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
