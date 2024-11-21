import boto3
from datetime import datetime, timedelta,timezone

# Initialize boto3 client for CloudTrail
client = boto3.client('cloudtrail')

# Define the time range
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(days=7)

# Function to get CloudTrail events
def get_cloudtrail_logs(start_time, end_time):
    paginator = client.get_paginator('lookup_events')
    response_iterator = paginator.paginate(
        StartTime=start_time,
        EndTime=end_time,
    )

    for response in response_iterator:
        events = response.get('Events', [])
        for event in events:
            # Extracting useful information from each event
            event_time = event.get('EventTime')
            event_name = event.get('EventName')
            user_identity = event.get('Username')
            event_source = event.get('EventSource')
            event_id = event.get('EventId')
            cloud_trail_event = event.get('CloudTrailEvent')

            # Printing the event information
            print(f"Event ID: {event_id}")
            print(f"Event Time: {event_time}")
            print(f"Event Name: {event_name}")
            print(f"User Identity: {user_identity}")
            print(f"Event Source: {event_source}")
            print("CloudTrail Event:")
            print(cloud_trail_event)
            print("="*60)

# Fetch and print CloudTrail logs
get_cloudtrail_logs(start_time, end_time)
