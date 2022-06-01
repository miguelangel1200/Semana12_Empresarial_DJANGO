from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Prestamo
from .serializers import PrestamoSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def prestamo_list(request):
        """
        List all code serie, or create a new serie.
        """
        if request.method == 'GET':
            series = Prestamo.objects.all()
            serializer = PrestamoSerializer(series, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PrestamoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)
            
    @csrf_exempt
    def prestamo_detail(request, pk):
        """
        Retrieve, update or delete a serie.
        """
        try:
            serie = Prestamo.objects.get(pk=pk)
        except Prestamo.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = PrestamoSerializer(serie)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = PrestamoSerializer(serie, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            serie.delete()
            return HttpResponse(status=204)
