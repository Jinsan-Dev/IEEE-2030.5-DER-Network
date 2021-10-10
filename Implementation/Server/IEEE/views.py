from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Device
from .serializer import DeviceSerializer

# Drawing a plot for monitor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def home(request):
    device = Device.objects.all()
    context = {
        'devices': device
    }
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

# Get system data that want to display from DB
def monitor(request):
    qe_dataFrame = pd.DataFrame(list(Device.objects.all().values()))    # Make Device as data frame
    time = qe_dataFrame['passedTime']                                   # passedTime column
    qe = qe_dataFrame['ess_Qe']                                         # ESS_Qe column
    plt.plot(time, qe)                                                  # Draw plot (X axis = time, Y axis = Qe)
    plt.xlabel('Time(sec)')
    plt.ylabel('Reactive Power(Var)')
    plt.title('Reactive power output of the ESS')
    plt.ylim(-1, 1)
    plt.grid()
    time_end = len(time.index)
    plt.yticks(np.arange(-1, 1.2, 0.5))
    plt.xticks(np.arange(0, time_end, 1))
    plt.savefig('/Users/Sane/Desktop/IEEE_2030_5/Server/SEP2/IEEE/static/graph/monitor.png')
    plt.close()

    return render(request, 'home/monitor.html', {'title': 'Monitor Devices'})

@api_view(['GET', 'POST'])
def systemDataList(request):
    if request.method == 'GET':
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   # After save,
            setCommand()        # Run setCommand func
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Set command to POSTed data
def setCommand():
    device = Device.objects.order_by().last()   # lastest data
    device.command = device.batteryStatus       # Right now, set command value same as batteryStatus
    device.save()

# Hand over certain command (pk=id) to client via GET method
@api_view(['GET'])
def getCommand(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return HttpRequest(status=404)

    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)