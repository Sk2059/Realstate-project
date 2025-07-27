from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    property_type = models.CharField(max_length=50, choices=[
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('land', 'Land'),
        ('commercial', 'Commercial')], default='house')
    for_type = models.CharField(max_length=50, choices=[
        ('select', 'Select'),
        ('sale', 'For Sale'),
        ('rent', 'For Rent')], default='select')
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    featured_image1 = models.ImageField(upload_to='properties/featured/', blank=True, null=True)
    featured_image2 = models.ImageField(upload_to='properties/featured/', blank=True, null=True)

    features = models.ManyToManyField(Feature, related_name='properties', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

