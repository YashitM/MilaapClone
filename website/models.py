from django.db import models


# Create your models here.
class Cause(models.Model):
    title_text = models.TextField()
    post_creator = models.CharField(max_length=100)
    amount_goal = models.IntegerField()
    detailed_description = models.TextField()
    title_image = models.ImageField(upload_to="media/images")
    already_funded = models.IntegerField()





