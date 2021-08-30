from django.db import models
from django.core import exceptions

from mptt import models as mptt_models


class AddedUpdatedTimeMixin(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AddedUpdatedTimeMixin, mptt_models.MPTTModel):
    """ Relations """
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    """ Data fields """
    name = models.CharField(max_length=255)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{ self.name }"


class Staff(AddedUpdatedTimeMixin, models.Model):
    """ Relations """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    """ Data fields """
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    job_started_time = models.DateField()
    salary = models.FloatField()

    @property
    def get_user_data(self):
        return f"Должность: { self.position }\nВремя начало работы: { self.job_started_time }\nЗП: { self.salary } р."

    def __str__(self):
        return f"{ self.full_name } -> { self.department.name }({ self.position })"
