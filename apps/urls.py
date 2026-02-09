
from django.urls import path
from apps.views import (StaticsViews, ServiceListView, ServiceRetrieveView,
                        ReviewListAPIView, LocationListAPIView, RefillOrderCreateAPIView, ResourceAPIList,
                        BlogListAPIView,BlogDetailAPIView,ContactRequestCreateAPIView)


urlpatterns = [
    path(
        "statistics/",
        StaticsViews.as_view(),
        name = 'statistika'
    ),
    path(
        "servive-list/",
        ServiceListView.as_view(),
        name = 'service-list'
    ),
    path(
        "servive-detail/<int:id>",
        ServiceRetrieveView.as_view(),
        name = 'service-detail'
    ),
    path(
        "review-list/",
        ReviewListAPIView.as_view(),
        name = 'review-list'
    ),
    path(
        "location-list/",
        LocationListAPIView.as_view(),
        name = 'location-list'
    ),
    path(
        "order/create",
        RefillOrderCreateAPIView.as_view(),
        name = 'order-create'
    ),
    path(
        'resource-list',
        ResourceAPIList.as_view(),
        name = 'resource-list'
    ),
    path(
        'blog-list',
        BlogListAPIView.as_view(),
        name = 'blog-list'
    ),
    path(
        'blog-detail/<int:id>',
        BlogDetailAPIView.as_view(),
        name = 'blog-detail'
    ),
    path(
        'contact-create',
        ContactRequestCreateAPIView.as_view(),
        name = 'contact-create'
    )


]
