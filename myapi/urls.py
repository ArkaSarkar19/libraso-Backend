from django.urls import include, path
from rest_framework import routers
from . import views
from .models import Fine

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'fines', views.FinesViewSet)
router.register(r'Issued', views.IssuedViewSet)
router.register(r'complaint', views.complaintViewSet)
router.register(r'Event', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("userfine/<int:id>/", views.get_fine_user, name = "get_fine_user"),
    path('event/<str:event_date>', views.get_event, name = "get_event"),
    path("books/<int:id>", views.issued_books)
    # path('userfine/update/<int:id>', views.update_fine_user)
]   