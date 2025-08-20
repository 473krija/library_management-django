from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'profiles', MemberProfileViewSet)
router.register(r'clubs', ReadingClubViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/fines/', FineListCreateView.as_view(), name='fine_list_create'),
    path('api/fines/<int:pk>/', FineDetailView.as_view(), name='fine_detail'),
]