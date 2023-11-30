from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("newspaper:redactor-detail", kwargs={"pk": self.pk})


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspaper")

    class Meta:
        ordering = ("title", )

    def __str__(self):
        return f"{self.title} (content: {self.content}, published date: {self.published_date})"

    def get_absolute_url(self):
        return reverse("newspaper:newspaper-details", args=[str(self.id)])
