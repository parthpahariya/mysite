from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_id = models.CharField(max_length=200, primary_key=True)
    x_coor = models.IntegerField()
    y_coor = models.IntegerField()

    def updateLocation(driverId, xCoor, yCoor):
        Driver(driver_id=driverId, x_coor= xCoor, y_coor = yCoor).save()

    def driverWithinRadius(radius, xCoor, yCoor):
        return Driver.objects.filter(
            x_coor__gte = xCoor - radius).filter(
            x_coor__lt = xCoor + radius).filter(
            y_coor__gte = yCoor - radius).filter(
            y_coor__lte = yCoor + radius)

    def getAll():
        return Driver.objects.all()
