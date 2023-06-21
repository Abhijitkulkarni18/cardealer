from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)  # Name of the car
    description = models.TextField()  # Description of the car

    def __str__(self):
        return self.name  # String representation of the car object

class Dealer(models.Model):
    name = models.CharField(max_length=200)  # Name of the dealer
    description = models.TextField()  # Description of the dealer

    def __str__(self):
        return self.name  # String representation of the dealer object

class Sales(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Car being sold (foreign key to Car model)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)  # Dealer making the sale (foreign key to Dealer model)
    description = models.TextField()  # Description of the sales transaction
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of creation

    def __str__(self):
        return f"{self.dealer.name} sold {self.car.name} on {self.created_at}"  # String representation of the sale object
