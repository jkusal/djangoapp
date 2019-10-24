from django.contrib import admin

from studenci import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Miasto)
admin.site.register(models.Uczelnia)
