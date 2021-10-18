from django.contrib import admin

from .models import Contact, Course,Branch, Category

admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Branch)
