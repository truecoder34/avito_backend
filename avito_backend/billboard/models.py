from django.db import models
import uuid
# Create your models here.

#base model-will not be created in db
class Entity(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    #is_deleted = models.BooleanField()

    class Meta:
        abstract = True


class Advertisement(Entity):
    title = models.CharField(blank=False,
                             max_length=200,
                             verbose_name="Advertisement title")
    description = models.TextField(blank=True,  # optional, blank = true means can be empty,
                                   max_length=1000,
                                   verbose_name="Description")
    def __str__(self):
        return "%s %s" % (self.id, self.title)

    class Meta:
        ordering = ['datetime_create']

class PhotoLinks(Entity):
    advertisement = models.ForeignKey(Advertisement,
                                      on_delete=models.CASCADE)
    photo_link = models.CharField(blank=False,
                                  max_length=500,
                                  verbose_name="Link on the photo")
    photo_number = models.IntegerField(blank=False)

    def __str__(self):
        return "%s link to advertisement %s" % (self.id, self.advertisement)