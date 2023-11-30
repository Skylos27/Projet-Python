from django.urls import path
from .views import CustomLoginView, page_vierge

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', page_vierge, name='page_vierge'),
]
