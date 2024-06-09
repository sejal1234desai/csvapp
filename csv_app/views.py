import pandas as pd
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import CSVFile
from django.conf import settings
import os

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('process_csv')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})

def process_csv(request):
    csv_file = CSVFile.objects.latest('uploaded_at')
    file_path = os.path.join(settings.MEDIA_ROOT, csv_file.file.name)
    
    # Try to read the CSV file with different encodings
    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    df = None
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding, on_bad_lines='skip')
            break
        except (UnicodeDecodeError, pd.errors.ParserError):
            continue

    if df is None or df.empty:
        return render(request, 'error.html', {'message': 'Could not read the CSV file or the file is empty.'})

    # Basic Data Analysis
    data_head = df.head().to_html()
    summary_stats = df.describe().to_html()

    # Convert missing values Series to DataFrame
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ['Column', 'Missing Values']
    missing_values_html = missing_values.to_html(index=False)

    # Data Visualization
    import matplotlib.pyplot as plt
    import seaborn as sns
    import io
    import urllib, base64

    plt.switch_backend('Agg')
    
    numerical_cols = df.select_dtypes(include=['number', 'datetime']).columns
    if not numerical_cols.empty:
        fig, ax = plt.subplots()
        df[numerical_cols].hist(ax=ax)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        plot_uri = uri
    else:
        plot_uri = None

    context = {
        'data_head': data_head,
        'summary_stats': summary_stats,
        'missing_values': missing_values_html,
        'plot_uri': plot_uri,
    }
    return render(request, 'results.html', context)
