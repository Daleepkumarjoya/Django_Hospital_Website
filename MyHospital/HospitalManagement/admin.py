from django.contrib import admin
from .models import HomeModel, ServicesModel, AboutModel, DoctorsModel, BookModel, ReviewModel, ContactModel, commentModel


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('DoctorName', 'DoctorExpertize')
    search_fields = ['DoctorName']
    list_filter = ['DoctorName']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'number')
    search_fields = ['first_name']
    list_filter = ['first_name']


admin.site.register(HomeModel)
admin.site.register(ServicesModel)
admin.site.register(AboutModel)
admin.site.register(DoctorsModel, DoctorAdmin)
admin.site.register(BookModel)
admin.site.register(ReviewModel)
admin.site.register(commentModel)
admin.site.register(ContactModel, ContactAdmin)
