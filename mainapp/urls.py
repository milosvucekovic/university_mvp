from django.urls import path
from .views import crud

urlpatterns = [
    # Program URLs
    path('', crud.ProgramListView.as_view(), name='program_list'),
    path('program/<int:pk>/', crud.ProgramDetailView.as_view(), name='program_detail'),
    path('program/create/', crud.ProgramCreateView.as_view(), name='program_create'),
    path('program/<int:pk>/update/', crud.ProgramUpdateView.as_view(), name='program_update'),
    path('program/<int:pk>/delete/', crud.ProgramDeleteView.as_view(), name='program_delete'),

    # About page
    path('about/', crud.AboutView.as_view(), name='about'),

    # University URLs
    path('university/', crud.UniversityListView.as_view(), name='university_list'),
    path('university/<int:pk>/', crud.UniversityDetailView.as_view(), name='university_detail'),
    path('university/create/', crud.UniversityCreateView.as_view(), name='university_create'),
    path('university/<int:pk>/update/', crud.UniversityUpdateView.as_view(), name='university_update'),
    path('university/<int:pk>/delete/', crud.UniversityDeleteView.as_view(), name='university_delete'),

    # Category URLs
    path('category/', crud.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', crud.CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', crud.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', crud.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', crud.CategoryDeleteView.as_view(), name='category_delete'),

    # ProgramApplication URLs
    path('programapplication/', crud.ProgramApplicationListView.as_view(), name='programapplication_list'),
    path('programapplication/<int:pk>/', crud.ProgramApplicationDetailView.as_view(), name='programapplication_detail'),
    path('programapplication/create/', crud.ProgramApplicationCreateView.as_view(), name='programapplication_create'),
    path('programapplication/<int:pk>/update/', crud.ProgramApplicationUpdateView.as_view(), name='programapplication_update'),
    path('programapplication/<int:pk>/delete/', crud.ProgramApplicationDeleteView.as_view(), name='programapplication_delete'),

    # ProgramSubmission URLs
    path('programsubmission/', crud.ProgramSubmissionListView.as_view(), name='programsubmission_list'),
    path('programsubmission/<int:pk>/', crud.ProgramSubmissionDetailView.as_view(), name='programsubmission_detail'),
    path('programsubmission/create/', crud.ProgramSubmissionCreateView.as_view(), name='programsubmission_create'),
    path('programsubmission/<int:pk>/update/', crud.ProgramSubmissionUpdateView.as_view(), name='programsubmission_update'),
    path('programsubmission/<int:pk>/delete/', crud.ProgramSubmissionDeleteView.as_view(), name='programsubmission_delete'),

    # Payment URLs
    path('payment/', crud.PaymentListView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', crud.PaymentDetailView.as_view(), name='payment_detail'),
    path('payment/create/', crud.PaymentCreateView.as_view(), name='payment_create'),
    path('payment/<int:pk>/update/', crud.PaymentUpdateView.as_view(), name='payment_update'),
    path('payment/<int:pk>/delete/', crud.PaymentDeleteView.as_view(), name='payment_delete'),

]