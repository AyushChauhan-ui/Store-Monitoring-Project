# store_monitoring_app/helpers.py

from store_monitoring_app.models import ReportData  # Import the model for the report data

def report_is_generated(report_id):
    # Check if a report with the given report_id exists in the database
    return ReportData.objects.filter(report_id=report_id).exists()

def get_report_data(report_id):
    # Fetch the report data for the given report_id from the database
    try:
        report_data = ReportData.objects.get(report_id=report_id)
    except ReportData.DoesNotExist:
        return None

    # Convert the report_data object to the required format (dictionary)
    return {
        'store_id': report_data.store_id,
        'uptime_last_hour': report_data.uptime_last_hour,
        'uptime_last_day': report_data.uptime_last_day,
        'uptime_last_week': report_data.uptime_last_week,
        'downtime_last_hour': report_data.downtime_last_hour,
        'downtime_last_day': report_data.downtime_last_day,
        'downtime_last_week': report_data.downtime_last_week,
    }
