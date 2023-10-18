from django.urls import path
from . import views

# if a request reaches /january ==> then execute, the views.index function. 
# this is called url config or url
urlpatterns = [
    path("", views.index), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]