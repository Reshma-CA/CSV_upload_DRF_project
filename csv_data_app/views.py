from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# def Welcome_page(request):
#     return render(request, 'csv_app_data/index.html') 
class IndexView(TemplateView):
    template_name = "csv_app_data/index.html"

import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import User_Model_Serializer

class Upload_CSV_data_View(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({'error': 'Invalid file type. Only CSV is allowed.'}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        total_records = 0
        saved_records = 0
        rejected_records = 0
        errors = []

        for row in reader:
            total_records += 1
            serializer = User_Model_Serializer(data=row)
            if serializer.is_valid():
                serializer.save()
                saved_records += 1
            else:
                rejected_records += 1
                errors.append({'row': row, 'errors': serializer.errors})

        response_data = {
            'total_records': total_records,
            'saved_records': saved_records,
            'invalid_records': rejected_records,
            'errors': errors
        }
        return Response(response_data, status=status.HTTP_200_OK)
