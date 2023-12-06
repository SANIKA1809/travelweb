from django.urls import path, include
from .views import review_list, submit_review, send_email, Kashmir, Kashmirtrip, Kashmirtrip1, Rome, Rometrip, Paris, Paristrip, Paristrip1

from . import views
from . import views as main_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('city', views.CityViewSet, basename='city')
router.register('itinerary', views.ItineraryViewSet, basename='itinerary')
urlpatterns = router.urls

urlpatterns = [
    # path("backend/", views.index, name="index"),
    path('api/', include(router.urls)),
    path('home/', views.home_screen, name = "home_screen"),
    path('city/', views.city_screen, name = "city_screen"),
    path('room/', views.home_screen, name = "room_screen"),
    path('home/check', main_views.check, name="button"),
    path('home/room/delete_row/<int:row_id>/', main_views.delete_row, name='delete_row'),
    path('home/room/update_row/<int:row_id>/<str:activity>/', main_views.update_row, name='delete_row'),
    path('reviews/', review_list, name='review_list'),
    path('submit_review/', submit_review, name='submit_review'),
    path('send_email/', send_email, name='send_email'),
    path('Kashmirtrip/', Kashmirtrip, name='Kashmirtrip'),
    path('Kashmirtrip1/', Kashmirtrip1, name='Kashmirtrip1'),
    path('Rome/', Rome, name='Rome'),
    path('Rometrip/', Rometrip, name='Rometrip'),
    path('Paris/', Paris, name='Paris'),
    path('Paristrip/', Paristrip, name='Paristrip'),
    path('Paristrip1/', Paristrip1, name='Paristrip1'),
    path('Kashmir/', Kashmir, name='Kashmir'),
    
]