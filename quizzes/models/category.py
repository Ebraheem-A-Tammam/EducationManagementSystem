from django.utils.text import slugify
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.category

def category_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.category)

models.signals.pre_save.connect(category_pre_save, sender=Category)