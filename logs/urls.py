from django.urls import path
from .views import (
    BloodLogByDateView, MedicationLogByDateView, MoodLogByDateView, SexualIntercourseLogCreateView, SexualIntercourseLogListView, SexualIntercourseLogDetailView,
    MoodLogCreateView, MoodLogListView, MoodLogDetailView,
    BloodFlowLogCreateView, BloodFlowLogListView, BloodFlowLogDetailView,
    MedicationLogCreateView, MedicationLogListView, MedicationLogDetailView, SymptomLogByDateView,
    SymptomLogCreateView, SymptomLogListView, SymptomLogDetailView, SexualIntercourseLogByDateView
    
)

urlpatterns = [
    # Sexual Intercourse Log URLs
    path('sexual-intercourse/', SexualIntercourseLogCreateView.as_view(), name='sexual-intercourse-create'),
    path('sexual-intercourse/list/', SexualIntercourseLogListView.as_view(), name='sexual-intercourse-list'),
    path('sexual-intercourse/date/', SexualIntercourseLogByDateView.as_view(), name='sexual-intercourse-by-date'),
    path('sexual-intercourse/<int:pk>/', SexualIntercourseLogDetailView.as_view(), name='sexual-intercourse-detail'),

    # Mood Log URLs
    path('mood/', MoodLogCreateView.as_view(), name='mood-create'),
    path('mood/list/', MoodLogListView.as_view(), name='mood-list'),
    path('mood/date/', MoodLogByDateView.as_view(), name='mood-by-date'),
    path('mood/<int:pk>/', MoodLogDetailView.as_view(), name='mood-detail'),

    # Blood Flow Log URLs
    path('blood-flow/', BloodFlowLogCreateView.as_view(), name='blood-flow-create'),
    path('blood-flow/list/', BloodFlowLogListView.as_view(), name='blood-flow-list'),
    path('blood-flow/date/', BloodLogByDateView.as_view(), name='blood-flow-by-date'),
    path('blood-flow/<int:pk>/', BloodFlowLogDetailView.as_view(), name='blood-flow-detail'),

    # Medication Log URLs
    path('medication/', MedicationLogCreateView.as_view(), name='medication-create'),
    path('medication/list/', MedicationLogListView.as_view(), name='medication-list'),
    path('medication/date/', MedicationLogByDateView.as_view(), name='medication-by-date'),
    path('medication/<int:pk>/', MedicationLogDetailView.as_view(), name='medication-detail'),

    # Symptom Log URLs
    path('symptom/', SymptomLogCreateView.as_view(), name='symptom-create'),
    path('symptom/list/', SymptomLogListView.as_view(), name='symptom-list'),
    path('symptom/date/', SymptomLogByDateView.as_view(), name='symptom-by-date'),
    path('symptom/<int:pk>/', SymptomLogDetailView.as_view(), name='symptom-detail'),
]