# core/urls.py
from django.urls import path
from .views import HomeView, CreateListing, ListingView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-listing', CreateListing.as_view(), name='add_listing'),
    path('listings/<slug:slug>/', ListingView.as_view(), name='listing'),
]

# mais legal pagina inicial path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
