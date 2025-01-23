
from django.urls import path,include
from .import views
from csv_data_app.views import Upload_CSV_data_View,IndexView,DetailsView

urlpatterns = [
    path('api/upload/', Upload_CSV_data_View.as_view(), name='upload_csv'),  # For uploading CSV
    path('', IndexView.as_view(template_name="csv_app_data/index.html"), name='index'),  # Index view
    path('details/', DetailsView, name='details'),  # For rendering the record details page
]


