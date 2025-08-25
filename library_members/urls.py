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

    # HTML Template Views
    path('memberprofiles/', member_list, name='member_list'),
    path('memberprofiles/<int:pk>/', member_detail, name='member_detail'),

    path('readingclubs/', club_list, name='club_list'),
    path('readingclubs/<int:pk>/', club_detail, name='club_detail'),

    path('fines/', fine_list, name='fine_list'),
    path('fines/<int:pk>/', fine_detail, name='fine_detail'),
]