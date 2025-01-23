from django.shortcuts import render
from django.views.generic import TemplateView
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import User_Model_Serializer
from django.shortcuts import redirect
from urllib.parse import urlencode

from django.http import HttpResponse
from django.template.loader import render_to_string
import json
# Create your views here.


class IndexView(TemplateView):
    template_name = "csv_app_data/index.html"

def DetailsView(request):
    return render(request, 'csv_app_data/record_details.html') 


class Upload_CSV_data_View(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        
        # Ensure the file is uploaded and is a CSV
        if not file:
            return Response({'error': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the file has a CSV extension
        if not file.name.endswith('.csv'):
            return Response({'error': 'Invalid file type. Only CSV files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decode and process the CSV file
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
                'errors': errors  # This holds rejected records and errors
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'File processing error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
         