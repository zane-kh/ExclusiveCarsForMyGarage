from pyexpat import model
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

from django.template import engines 

# Create your models here.

class Car(models.Model):
        # drop down 
        state_choice = (('CA', 'California'), ('NY', 'New York'), ('FL', 'Florida'), ('PA', 'Pennsylvania'),) 
        
        year_choice = []
        for r in range(2000, (datetime.now().year+1)):
            year_choice.append((r,r))
            
        features_choices = (('Wind Deflector', 'Wind Deflector'), ('Parking Assist', 'Parking Assist'))
        
        door_choices = (('2', '2'),)
        
        car_title = models.CharField(max_length=255)
        color = models.CharField(max_length=100, default='black')
        state = models.CharField(choices=state_choice, max_length=100)
        city = models.CharField(max_length=100)
        model = models.CharField(max_length=100)
        year = models.IntegerField(choices=year_choice)
        condition = models.CharField(max_length=100)
        price = models.IntegerField()
        description = RichTextField()
        car_photo = models.ImageField(upload_to='photos/%Y/%M/%D/')
        car_photo_1 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
        car_photo_2 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
        car_photo_3 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
        car_photo_4 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
        features = MultiSelectField(choices=features_choices)
        body_style = models.CharField(max_length=100)
        engine = models.CharField(max_length=100)
        transmission = models.CharField(max_length=100)
        interior = models.CharField(max_length=100)
        miles = models.IntegerField()
        doors = models.CharField(choices=door_choices, max_length=10)
        passengers = models.IntegerField()
        vin_no = models.CharField(max_length=100)
        mileage = models.IntegerField()
        fuel_type = models.CharField(max_length=50)
        no_of_owners = models.CharField(max_length=100)
        is_featured = models.BooleanField(default = False)
        is_informed_buyer = models.BooleanField(default=False, blank=True)
        created_date = models.DateTimeField(default=datetime.now, blank=True)
        
        def __str__(self):
                return self.car_title
        
        
        
