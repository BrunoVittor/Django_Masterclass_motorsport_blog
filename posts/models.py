from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
	title = models.CharField(max_length=150)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.title)

	def post_count(self):
		return self.posts.all().count()


class SportCars(models.Model):
	model_car = models.CharField(max_length=200)
	manufacturer = models.CharField(max_length=200)
	color_car = models.CharField(max_length=100)
	details_car = models.TextField()
	data = models.DateTimeField(auto_now_add=True)
	image_car = models.ImageField(null=True, blank=True, upload_to='images')
	slug = models.SlugField(default='slug', editable=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.model_car)
		super(SportCars, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.model_car) + ' - ' + str(self.manufacturer)
