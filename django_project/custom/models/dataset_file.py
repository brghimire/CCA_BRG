# coding=utf-8
"""Datasets files model definition.
"""
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField

CSV = 'csv'
VECTORS = 'vectors'
RASTER = 'raster'

class DatasetFile(models.Model):
    """Datasets files model"""

    FUNC_CHOICES = (
        (CSV, 'CSV'),
        (VECTORS, 'Vectors'),
        (RASTER, 'Raster')
    )

    dataset = models.ForeignKey(
        'custom.Dataset',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    endpoint = models.FileField(
        upload_to='datasets/',
    )

    label = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    configuration = JSONField(
        null=True,
        blank=True
    )

    test = models.BooleanField(
        default=False
    )

    comment = models.TextField(
        default='',
        blank=True
    )

    active = models.BooleanField(
        default=False
    )

    func = models.CharField(
        max_length=50,
        choices=FUNC_CHOICES,
        default='',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dataset_file_created_by'
    )

    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='dataset_file_updated_by'
    )

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'Dataset Files'