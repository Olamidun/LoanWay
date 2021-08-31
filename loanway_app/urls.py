from . import views
from django.urls import path

app_name='loanway_app'

urlpatterns = [
    path('apply', views.approve_or_reject_loan),
    path('your_applications', views.ListUserAppliedLoans.as_view()),
    path('your_application/<int:id>', views.RetrieveUserAppliedLoans.as_view())
]