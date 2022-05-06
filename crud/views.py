from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import SpatialData
from .serializers import SpatialDataSerializer
from .common import india
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry

# Create your views here.

class SpatialDataAPI(APIView):
    def get_object(self, pk):
        try:
            return SpatialData.objects.get(ADMIN=pk)
        except SpatialData.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SpatialDataSerializer(data)

        else:
            data = SpatialData.objects.all()
            serializer = SpatialDataSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SpatialDataSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Record Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        todo_to_update = SpatialData.objects.get(ADMIN=pk)
        serializer = SpatialDataSerializer(instance=todo_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Record Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        todo_to_delete = SpatialData.objects.get(ADMIN=pk)

        todo_to_delete.delete()

        return Response({
            'message': 'Record Deleted Successfully'
        })



class SpatialQueryAPI(APIView):

    def get(self, request, pk=None, format=None):
        query = GEOSGeometry(india)
        intersection_loc = []

        for region in SpatialData.objects.filter(location__intersects=query):
            intersection_loc.append((region))

        total_countries = len(intersection_loc)
        result = ""
        if total_countries > 1:
            for each in intersection_loc:
                #if str(each).lower == "india":
                #    continue
                result = result + str(each) + ", "
            result = "Countries intersecting with India are - " + result
        else:
            result = "No Country is intersecting with India"


        return Response({
            'message': result
        })



class NonSpatialQueryAPI(APIView):

    def get(self, request, pk, format=None):
        countries = ""
        for each in SpatialData.objects.filter(ADMIN__icontains = pk):
            countries = countries + str(each) + ", "

        if countries == "":
            result = "No country avaiable with name : " + pk
        else:
            result = "Countris available with name " + pk + " are - " + countries


        return Response({
            'message': result
        })