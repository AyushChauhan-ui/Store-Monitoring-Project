import requests

# Replace this with the appropriate base URL of your Django server
base_url = 'http://127.0.0.1:8000/'

# Endpoint for triggering the report generation
trigger_report_url = f'{base_url}api/trigger_report'

# Endpoint for fetching the report data
get_report_url = f'{base_url}api/get_report'

try:
    # Make the POST request to trigger the report generation
    response = requests.post(trigger_report_url)

    # Check if the response status code is successful (2xx)
    response.raise_for_status()

    # Get the response data in JSON format
    data = response.json()

    # Print the report_id
    report_id = data['report_id']
    print('Report ID:', report_id)

    try:
        # Make the GET request to fetch the report data using the report_id
        response = requests.get(get_report_url, params={'report_id': report_id})

        # Check if the response status code is successful (2xx)
        response.raise_for_status()

        # Get the response data in JSON format
        data = response.json()

        # Print the report status and report data (if available)
        print('Report Status:', data['status'])
        print('Report Data:', data.get('report_data'))

    except requests.exceptions.HTTPError as err:
        print('Error fetching report data:', err)

except requests.exceptions.HTTPError as err:
    print('Error triggering report generation:', err)

except requests.exceptions.JSONDecodeError as err:
    print('Error decoding JSON response:', err)
