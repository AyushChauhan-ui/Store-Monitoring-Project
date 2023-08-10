# store_monitoring_app/views.py
# store_monitoring_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from store_monitoring_app.models import StoreStatus, BusinessHours, StoreTimezone
from store_monitoring_app.report_computation import compute_report
from store_monitoring_app.report_generator import generate_report
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Welcome to the Store Monitoring API!'})

@csrf_exempt
def trigger_report(request):
    # Trigger the report generation (you can generate a random report_id)
    report_id = "your_generated_report_id"
    generate_report(report_id)  # Call the function to generate the report asynchronously
    return JsonResponse({'report_id': report_id})

def get_report(request):
    report_id = request.GET.get('report_id')
    # Check if the report is generated and return the report data
    # You can implement the logic to fetch and compute the report data from the database
    if report_is_generated(report_id):
        report_data = get_report_data(report_id)
        return JsonResponse({'status': 'Complete', 'report_data': report_data})
    else:
        return JsonResponse({'status': 'Running'})

def report_is_generated(report_id):
    # Implement the logic to check if the report with the given report_id is generated
    # You can use a model field or a separate table to store the status of the report generation
    # For example, if you have a model for storing the report status:
    return YourReportStatusModel.objects.filter(report_id=report_id, is_generated=True).exists()

def get_report_data(report_id):
    # Implement the logic to fetch the report data from the database
    # You can retrieve the report data using the report_id as a parameter
    # For example, if you have a model for storing the report data:
    try:
        report_data = YourReportDataModel.objects.get(report_id=report_id)
        return report_data.report_data
    except YourReportDataModel.DoesNotExist:
        return None

