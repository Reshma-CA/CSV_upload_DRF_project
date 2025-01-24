import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_upload_csv_valid(api_client):
   
    # Prepare valid CSV data
    csv_data = 'name,email,age\nreshma ca,reshma.ca@example.com,29\nanu K,anuk.s@example.com,25'
    
    # Create a file-like object from CSV data
    from io import StringIO
    from django.core.files.uploadedfile import InMemoryUploadedFile

    file = InMemoryUploadedFile(StringIO(csv_data), None, 'test.csv', 'text/csv', len(csv_data), None)
    
    # Send a POST request to upload the CSV
    url = reverse('upload_csv')  # Adjust the name based on your URL configuration
    response = api_client.post(url, {'file': file}, format='multipart')
    
    # Validate the response status
    assert response.status_code == status.HTTP_200_OK

    # Validate the response data
    data = response.json()
    assert data['total_records'] == 2  # 2 records in the CSV
    assert data['saved_records'] == 2  # All records should be saved
    assert data['invalid_records'] == 0  # No invalid records

@pytest.mark.django_db
def test_upload_csv_invalid_file(api_client):

    
    # Create a fake Word file
    from io import BytesIO
    file = BytesIO(b"Some random content that is not CSV format")
    file.name = 'test.docx'
    
    # Send a POST request to upload the invalid file
    url = reverse('upload_csv')  # Adjust the name based on your URL configuration
    response = api_client.post(url, {'file': file}, format='multipart')
    
    # Validate the response status
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Validate the error message
    data = response.json()
    assert data['error'] == 'Invalid file type. Only CSV files are allowed.'
