from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Catégorie"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*arg, **kwargs)


# Create your models here.
class Serie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    category = models.ManyToManyField(Category)
    seen_seasons = models.IntegerField(default=0)
    number_of_seasons = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Série"
        verbose_name_plural = "Toutes les séries"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.seen_seasons} / {self.number_of_seasons}"

    @property
    def nb_seasons_string(self):
        if self.name:
            return f"La série {self.name} a {self.number_of_seasons} saison{'s' if self.number_of_seasons > 1 else '' }"
        return "Cette série n'est pas dans la base de donnée"

    def save(self, *arg, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*arg, **kwargs)



