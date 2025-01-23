
from django.urls import path,include
from .import views
from csv_data_app.views import Upload_CSV_data_View,IndexView

urlpatterns = [

    path('api/upload/', Upload_CSV_data_View.as_view(), name='upload_csv'),
    path('', IndexView.as_view(template_name="csv_app_data/index.html"), name='index'),
    # path("",views.Welcome_page,name="welcome"),
   
    
]