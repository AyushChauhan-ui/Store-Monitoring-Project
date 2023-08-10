
from datetime import timedelta
from django.utils import timezone

def compute_report(store_status_data, business_hours_data, store_timezone_data):
    report_data = {}

    for store_timezone in store_timezone_data:
        store_id = store_timezone.store_id
        timezone_str = store_timezone.timezone_str

        store_status = store_status_data.filter(store_id=store_id)
        business_hours = business_hours_data.filter(store_id=store_id)

        report_data[store_id] = {
            'uptime_last_hour': 0,
            'uptime_last_day': 0,
            'uptime_last_week': 0,
            'downtime_last_hour': 0,
            'downtime_last_day': 0,
            'downtime_last_week': 0,
        }

        current_time = timezone.now().astimezone(timezone.get_timezone(timezone_str))
        last_hour_threshold = current_time - timedelta(hours=1)
        last_day_threshold = current_time - timedelta(days=1)
        last_week_threshold = current_time - timedelta(weeks=1)

        for business_hour in business_hours:
            start_time = current_time.replace(hour=business_hour.start_time_local.hour, minute=business_hour.start_time_local.minute)
            end_time = current_time.replace(hour=business_hour.end_time_local.hour, minute=business_hour.end_time_local.minute)

            total_duration = end_time - start_time
            active_duration = timedelta()
            inactive_duration = timedelta()

            for status_entry in store_status:
                status_time = status_entry.timestamp_utc.astimezone(timezone.get_timezone(timezone_str))

                if status_time >= end_time:
                    break

                if status_time >= start_time:
                    if status_time <= end_time:
                        active_duration += timedelta(minutes=60)
                    else:
                        active_duration += end_time - status_time
                else:
                    inactive_duration += min(status_time, end_time) - max(status_time, start_time)

            uptime_last_hour = min(active_duration, timedelta(minutes=60))
            uptime_last_day = min(active_duration, total_duration)
            uptime_last_week = min(active_duration, total_duration * 7)

            downtime_last_hour = min(inactive_duration, timedelta(minutes=60))
            downtime_last_day = min(inactive_duration, total_duration)
            downtime_last_week = min(inactive_duration, total_duration * 7)

            report_data[store_id]['uptime_last_hour'] += uptime_last_hour.total_seconds() // 60
            report_data[store_id]['uptime_last_day'] += uptime_last_day.total_seconds() // 3600
            report_data[store_id]['uptime_last_week'] += uptime_last_week.total_seconds() // 3600

            report_data[store_id]['downtime_last_hour'] += downtime_last_hour.total_seconds() // 60
            report_data[store_id]['downtime_last_day'] += downtime_last_day.total_seconds() // 3600
            report_data[store_id]['downtime_last_week'] += downtime_last_week.total_seconds() // 3600

    return report_data
