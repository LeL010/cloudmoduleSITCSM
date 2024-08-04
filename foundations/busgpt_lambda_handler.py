import json
import logging
import urllib3
from datetime import datetime, timedelta, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_bus_arrival(bus_stop_code, bus_number):
    base_url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"
    params = f"?BusStopCode={bus_stop_code}"
    if bus_number:
        params += f"&ServiceNo={bus_number}"
    api_url = base_url + params

    headers = {
        'AccountKey': 'L0rh7vMWQIyQ7ZLZkCBGEA==',
        'accept': 'application/json'
    }

    http = urllib3.PoolManager()
    response = http.request('GET', api_url, headers=headers)

    if response.status != 200 or not response.data:
        return f"Error: Received response status {response.status} from the API."

    try:
        data = json.loads(response.data.decode('utf-8'))
    except json.JSONDecodeError:
        return "Error: Failed to parse response from the API."

    def calculate_minutes_until(arrival_time_str):
        arrival_time = datetime.fromisoformat(arrival_time_str.replace("Z", "+00:00")).astimezone(timezone(timedelta(hours=8)))
        current_time = datetime.now(timezone(timedelta(hours=8)))
        time_diff = arrival_time - current_time
        return int(time_diff.total_seconds() // 60)

    def format_time(minutes):
        return "Arrived" if minutes <= 0 else f"{minutes} mins"

    if 'Services' in data and data['Services']:
        messages = []
        for service in data['Services']:
            service_no = service['ServiceNo']
            next_bus_time = format_time(calculate_minutes_until(service.get('NextBus', {}).get('EstimatedArrival', 'N/A')))
            next_bus2_time = format_time(calculate_minutes_until(service.get('NextBus2', {}).get('EstimatedArrival', 'N/A')))
            next_bus3_time = format_time(calculate_minutes_until(service.get('NextBus3', {}).get('EstimatedArrival', 'N/A')))
            messages.append(f"Service {service_no}: Next bus in {next_bus_time}, Next bus 2 in {next_bus2_time}, Next bus 3 in {next_bus3_time}.")
        message = " ".join(messages)
    else:
        message = f"No arrival information available for the bus stop {bus_stop_code}."

    return message

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        interpretations = event['interpretations']
        bus_stop_code = interpretations[0]['intent']['slots']['BusStopCode']['value']['originalValue']
        bus_number = interpretations[0]['intent']['slots']['BusNumber']['value']['originalValue']
        lexmessage = get_bus_arrival(bus_stop_code, bus_number)
    
    except KeyError as e:
        logger.error(f"KeyError: {str(e)} - Event structure: {json.dumps(event)}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                },
                "intent": {
                    "name": "BusArrivalIntent",
                    "state": "Failed"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": f"An error occurred: {str(e)}"
                }
            ]
        }
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)} - Event structure: {json.dumps(event)}")
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                },
                "intent": {
                    "name": "BusArrivalIntent",
                    "state": "Failed"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "An unexpected error occurred."
                }
            ]
        }
    
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
            },
            "intent": {
                "name": "BusArrivalIntent",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": lexmessage
            }
        ]
    }
