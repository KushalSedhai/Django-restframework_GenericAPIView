from django.urls import path
from .views import Studentview, StudentDetailView

urlpatterns = [
   path('Student/', Studentview.as_view() ),
   path('Student/<int:pk>/', StudentDetailView.as_view())
]
