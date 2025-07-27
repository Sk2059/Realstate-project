from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class ServiceRequest(models.Model):
    service_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100, choices=[
        ('select', 'select'),
        ('House renovation', 'House Renovation'),
        ('Interior painting', 'Interior Painting'),
        ('Exterior painting', 'Exterior Painting'),
        ('Kitchen renovation', 'Kitchen Renovation'),
        ('Bathroom renovation', 'Bathroom Renovation'),
        ('Other', 'Other')
    ])
    Service_urgency = models.CharField(max_length=100, choices=[
        ('select', 'select'),
        ('2 Weeks', '2 Weeks'),
        ('1 Month', '1 Month'),
        ('3 Months', '3 Months'),
    ])
    preffered_date = models.DateField()
    description = models.TextField()
    imag= models.ImageField(upload_to='service_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name    
    


class Sell(models.Model):  # ← Add inheritance
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    propert_title = models.CharField(max_length=200)
    property_location = models.CharField(max_length=255)
    property_price = models.CharField(max_length=20)
    property_type = models.CharField(max_length=100, choices=[
        ('select', 'select'),
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Condo', 'Condo'),
        ('townhouse', 'Townhouse'),
        ('Other', 'Other')
    ])
    no_of_bedrooms = models.IntegerField(null=True, blank=True)
    no_of_bathrooms = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.propert_title} - {self.name}"