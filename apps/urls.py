from django.conf.urls.static import static
from django.urls import path
from apps.views import StaticsViews, ServiceListView, ServiceRetrieveView
from config import settings

urlpatterns = [
    path("statistics/", StaticsViews.as_view(), name = 'statistika'),
    path("servive-list/", ServiceListView.as_view(), name = 'service-list'),
    path("servive-detail/<int:id>", ServiceRetrieveView.as_view(), name = 'service-detail'),


]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)