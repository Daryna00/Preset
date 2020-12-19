from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Merchandise(models.Model):
    name = models.CharField(max_length=64)
    about_preset = models.TextField(max_length=2048, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    before_img = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        width_field='width_field1',
        height_field='height_field1'
    )
    height_field1 = models.IntegerField(default=0)
    width_field1 = models.IntegerField(default=0)
    after_img = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        width_field='width_field2',
        height_field='height_field2'
    )
    height_field2 = models.IntegerField(default=0)
    width_field2 = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=False)
    cost = models.CharField(max_length=7)
    likes = models.ManyToManyField(User, related_name='like_list', null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-timestamp', '-updated']



def create_slug(instance: Merchandise, new_slug=None) -> str:
    slug = slugify(instance.name)

    if new_slug is not None:
        slug = new_slug
    qs = instance._meta.model.objects.filter(slug=slug).order_by('-id')
    duplicate_exist = qs.exists()
    if duplicate_exist:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_product_receiver(sender, instance: Merchandise, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(receiver=pre_save_product_receiver, sender=Merchandise)