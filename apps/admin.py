from django.contrib import admin
from apps.models import Statistics, Service,Review,RefillOrder,RefillItem,ExtraItem,Resource,BlogPost,ContactRequest, ServiceCategory
from apps.models.Location import Location,WorkHour


admin.site.register(Statistics)
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(WorkHour)
admin.site.register(Location)
admin.site.register(RefillOrder)
admin.site.register(RefillItem)
admin.site.register(ExtraItem)
admin.site.register(Resource)
admin.site.register(BlogPost)
admin.site.register(ContactRequest)
