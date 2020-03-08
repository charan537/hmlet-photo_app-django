from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
import os
from django.urls import reverse_lazy

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='./')
    captions = models.CharField(max_length=255,null=True, blank=True)
    publishedDate = models.DateTimeField(default=None,null=True, blank=True)
    saveAsDraft = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def get_absolute_url(self):
        if self.saveAsDraft == True:
            return reverse_lazy('photo_mydrafts')
        else:
            return reverse_lazy('photo_mylist')

@receiver(models.signals.post_delete, sender=Photo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `image` object is deleted.
    """
    if instance.image:
        img_url = instance.image.url
        file_path = os.path.join(settings.MEDIA_ROOT,img_url.replace(settings.MEDIA_URL,""))
        if os.path.isfile(file_path):
            os.remove(file_path)

@receiver(models.signals.pre_save, sender=Photo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `image` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_img_url = sender.objects.get(pk=instance.pk).image.url
        old_file_path = os.path.join(settings.MEDIA_ROOT,old_img_url.replace(settings.MEDIA_URL,""))
    except sender.DoesNotExist:
        return False

    new_img_url = os.path.join(settings.BASE_DIR,instance.image.url)
    new_file_path = os.path.join(settings.MEDIA_ROOT,new_img_url.replace(settings.MEDIA_URL,""))
    if not old_file_path == new_file_path:
        if os.path.isfile(old_file_path):
            os.remove(old_file_path)