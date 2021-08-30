from django.contrib import admin

from mptt import admin as mptt_admin

from . import models


@admin.register(models.Department)
class DepartmentAdmin(mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
