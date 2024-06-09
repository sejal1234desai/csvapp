This project is a Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.
Step 1: Install the Dependencies
* pip install django
* pip install django pandas numpy matplotlib seaborn
Step 2:
django-admin startproject myprojec
cd myproject
Step 3:
python manage.py startapp csvapp
Step 4:
Added csvapp to the INSTALLED_APPS in myproject/settings.py:
INSTALLED_APPS = [
    ...
    'csvapp',
]

 Step 5:
  URLs in myproject/urls.py to include csvapp URLs

  Step 6:
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('csvapp.urls')),
]

Step 7:
Implemented Views ,implemented the view for handling file upload and processing

Step 8:
Created templates in templates for the upload form and results display.

Project Infomation :
1. Django Setup:

* The project is built using the Django web framework.
* It includes a Django app within the project to manage the application's functionality.
2. File Upload:
* Users can upload CSV files through a form.
Data Processing:
* Displays the first few rows of the uploaded CSV data.
* Calculates summary statistics such as mean, median, and standard deviation for numerical columns.
* Identifies and handles missing values.
Data Visualization-
* generates and displays histograms for numerical columns using matplotlib or seaborn.
User Interface-
* Simple and user-friendly interface to display data analysis results and visualizations.
