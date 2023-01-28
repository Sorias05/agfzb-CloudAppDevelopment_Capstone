from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField('Name', max_length=150)
    description = models.CharField('Description', max_length=500)
    def __str__():
        return("Name: " + name + "\nDescription: " + description)

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=150)
    dealer_id = models.IntegerField(default=0)
    type = models.CharField('Type', max_length=150)
    year = models.DateField(default=now)
    def __str__():
        return("Name: " + name + "\nType: " + type + "\nYear: " + year + "\nMake: " + car_make + "\nDealer: " + dealer_id)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
