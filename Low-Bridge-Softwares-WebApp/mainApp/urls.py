from django.urls import path
from .views import renderIndex

urlpatterns = [
    path("",renderIndex,name="dashboard")
]