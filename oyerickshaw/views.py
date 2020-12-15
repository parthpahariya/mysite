from django.shortcuts import render
from django.http import HttpResponse

#models query
from .models import Driver

# Create your views here.

def index(request):
    return render(request, 'oyerickshaw/index.html')

def updateDrivesCoordinates(request):
    if request.method == 'POST':
        driverId = int(request.POST.get('driver_id'))
        xCoordinate = int(request.POST.get('x_value'))
        yCoordinate = int(request.POST.get('y_value'))


        drivers = Driver.updateLocation(driverId, xCoordinate, yCoordinate)
        arr = []
        context={"msg":arr}
        return render(request,'oyerickshaw/updatelocation.html',context)
    else:
        return render(request, 'oyerickshaw/updatelocation.html')

def getDriversWithinDistance(request):
    if request.method == 'POST':
        xCoordinate = int(request.POST.get('x_value'))
        yCoordinate = int(request.POST.get('y_value'))
        radius = int(request.POST.get('radius'))

        drivers = Driver.driverWithinRadius(radius, xCoordinate, yCoordinate)
        arr = []
        for div in drivers:
            dis = div.x_coor * div.x_coor + div.y_coor * div.y_coor
            if dis <= radius * radius:
                arr.append(div)
        context={"msg":arr}
        return render(request,'oyerickshaw/drivers.html',context)
    else:
        return render(request, 'oyerickshaw/drivers.html')

# def getLocationByDriverId(request, driverId):
#
#     return HttpResponse("You're looking at question %s, %s." % longitude % latidue)
#
# def results(request, userId, xCoordinate, yCoordinate):
#     # fetch drivers ids
#     #fetch location for drivers
#     #calculate distances and return map.
#
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

