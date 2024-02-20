from django.urls import path
from . import views

urlpatterns = [
		# ... your other paths
		path('register/', views.register, name='register'),
]
