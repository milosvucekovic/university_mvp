from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from mainapp.models import *
from django import forms

class ProgramListView(ListView):
    model = Program
    template_name = 'mainapp/landing_page.html'
    context_object_name = 'program_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = Program.objects.filter(is_published=True).select_related('university', 'category')
        
        # Get filter parameters
        search_query = self.request.GET.get('search', '')
        country = self.request.GET.get('country', '')
        category_id = self.request.GET.get('category', '')
        language = self.request.GET.get('language', '')

        # Apply search filter
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(university__name__icontains=search_query)
            )

        # Apply other filters
        if country:
            queryset = queryset.filter(country=country)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if language:
            queryset = queryset.filter(language=language)

        # Order by pinned status first, then by title
        return queryset.order_by('-is_pinned', 'title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get unique values for filters
        context['countries'] = Program.objects.filter(is_published=True).values_list('country', flat=True).distinct().exclude(country__isnull=True)
        context['categories'] = Category.objects.all()
        context['languages'] = Program.objects.filter(is_published=True).values_list('language', flat=True).distinct().exclude(language__isnull=True)
        
        return context

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
    success_url = reverse_lazy('program_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your application has been submitted successfully! We will contact you soon.')
        return response

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

class AboutView(TemplateView):
    template_name = 'mainapp/about.html'
