from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name='loanway_app'

urlpatterns = [
    path('/apply', views.approve_or_reject_loan),
    # path('/apply', views.CheckEligibilty.as_view()),
]