from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField(max_length=2048)
    max_presets = models.IntegerField(default=10)
    is_discount_preset = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field'
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'Product - {self.name}'

    class Meta:
        ordering = ['-timestamp', '-updated']


def create_slug(instance: Product, new_slug=None) -> str:
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug
    qs = instance._meta.model.objects.filter(slug=slug).order_by('-id')
    duplicate_exist = qs.exists()
    if duplicate_exist:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_product_receiver(sender, instance: Product, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(receiver=pre_save_product_receiver, sender=Product)