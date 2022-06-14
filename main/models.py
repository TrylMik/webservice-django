from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class SpotsPost(models.Model):
    class Meta:
            verbose_name = "Miejscówka"
            verbose_name_plural = "Miejscówki"

    title = models.CharField(max_length=255, verbose_name="Tytuł")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    body = models.TextField(verbose_name = "Treść")

    def get_absolute_url(self):
        return reverse('Spots')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class SpotsComment(models.Model):
    class Meta:
        verbose_name = "Komentarz do miejscówek"
        verbose_name_plural = "Komentarze do miejscówek"

    post = models.ForeignKey(SpotsPost, related_name="spotscomments", on_delete=models.CASCADE, verbose_name="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    body = models.TextField(verbose_name="Treść")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post) + ' | ' + str(self.author)


