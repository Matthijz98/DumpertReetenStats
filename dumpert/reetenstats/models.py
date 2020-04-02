from django.db import models
from filer.fields.image import FilerImageField

class Gast(models.Model):
    gast_name = models.CharField(max_length=64)
    gast_underline = models.CharField(max_length=64)
    gast_img = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
    gast_facebook = models.URLField()
    gast_instagram = models.URLField()
    gast_website = models.URLField()


class Show(models.Model):
    show_title = models.CharField(max_length=255)
    show_description = models.TextField()
    show_gasten = models.ManyToManyField(Gast)
    show_youtube_id = models.CharField(max_length=32)
    show_dumpert_id = models.CharField(max_length=32)


class Video(models.Model):
    video_title = models.CharField(max_length=255)
    video_description = models.TextField()
    video_dumpert_id = models.CharField(max_length=64)


class RatingType(models.Model):
    rating_type_name = models.CharField(max_length=128)


class Rating(models.Model):
    rating_in_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    rating_by = models.ForeignKey(Gast, on_delete=models.CASCADE)
    rating_type = models.ForeignKey(RatingType, on_delete=models.CASCADE)
    rating_ammount = models.DecimalField(max_digits=6, decimal_places=3)