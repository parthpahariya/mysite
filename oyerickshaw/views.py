from django.shortcuts import render
from django.http import HttpResponse

#models query
from .models import Driver

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def updateDrivesCoordinates(request, driverId, xCoordinate,  yCoordinate):
    return HttpResponse("You're looking at question %s, %s." % longitude % latidue)

def getDriversWithinDistance(request):
    if request.method == 'POST':
        xCoordinate = request.POST.get('x_value')
        yCoordinate = request.POST.get('y_value')

        drivers = Driver.driverWithinRadius(200, xCoordinate, yCoordinate)
        arr = []
        for div in drivers:
            dis = div.x_coor * div.x_coor + div.y_coor * div.y_coor
            if dis <= 40000:
                arr.append(div)
        return HttpResponse(arr)
    else:
        return render(request, 'polls/index.html')

def getLocationByDriverId(request, driverId):

    return HttpResponse("You're looking at question %s, %s." % longitude % latidue)

def results(request, userId, xCoordinate, yCoordinate):
    # fetch drivers ids
    #fetch location for drivers
    #calculate distances and return map.

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

