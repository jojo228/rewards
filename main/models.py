from django.db import models
from django.urls import reverse

class Photo(models.Model):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="products_photos")
    product = models.ForeignKey("Products", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
    

class Specification(models.Model):
    nom = models.CharField(max_length=80)
    product = models.ForeignKey("Products", related_name="specifications", on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Products(models.Model):
    name = models.CharField(max_length=140)
    price = models.IntegerField()
    description = models.TextField()
    video_link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})


    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos
    
    def get_all_specifications(self):
        specifications = self.specifications.all()
        return specifications