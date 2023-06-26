from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from secret_keys import *

# Authenticate and create a Google Calendar service instance
def authenticate():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    return service

# service = authenticate()

# Function to add events to a Google Calendar
def add_events_to_calendar(events):
    # service = authenticate() // not necessary anymore, done in globals but might still come in handy if the authentication cancels automatically
    # for event in events:
    #     event_body = {
    #         'summary': event['summary'],
    #         'start': {'dateTime': event['start']},
    #         'end': {'dateTime': event['end']}
    #     }
    #     service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
    print("\nEVENTS TO BE ADDED:")
    print(events)
    print()
    return "success"

# Function to retrieve events from a Google Calendar between specified start and end dates
def get_events_between_dates(start_date, end_date, keyword=None):
    #service = authenticate()

    # start_datetime = datetime.combine(start_date, datetime.min.time()).isoformat() + 'Z'
    # end_datetime = datetime.combine(end_date, datetime.max.time()).isoformat() + 'Z'

    # events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=start_datetime, timeMax=end_datetime,
    #                                       singleEvents=True, orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if keyword:
    #     filtered_events = [event for event in events if keyword.lower() in event.get('summary', '').lower()]
    #     return filtered_events
    # else:
    #     return events

    print("\nHERE ARE THE DATE PERIOD THAT WAS REQUIRED/")
    print(start_date)
    print(end_date)
    print("With the keyword: ", keyword)
    return input("What should the answer be?\n")

# Function to modify a specific event in a Google Calendar
def modify_event(event_id, new_data):
    #service = authenticate()

    # event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()
    # event.update(new_data)
    # updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event_id, body=event).execute()
    # return updated_event
    print("\nEVENT MODIFIED:")
    print(event_id)
    print(new_data)
    print()
    return "success"

def delete_events(event_ids):
    #service = authenticate()

    # event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()
    # event.update(new_data)
    # updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event_id, body=event).execute()
    # return updated_event
    print("\nEVENTs DELETED:")
    print(event_ids)
    print()
    return "success"

# Example usage
if __name__ == '__main__':
    events = [
        {
            'summary': 'Meeting',
            'start': '2023-06-27T10:00:00',
            'end': '2023-06-27T11:00:00'
        },
        {
            'summary': 'Appointment',
            'start': '2023-06-28T14:00:00',
            'end': '2023-06-28T15:00:00'
        }
    ]

    # Add events to the calendar
    add_events_to_calendar(events)

    # Retrieve events between specified dates
    start_date = datetime(2023, 6, 26).date()
    end_date = datetime(2023, 6, 29).date()
    events_between_dates = get_events_between_dates(start_date, end_date)
    print("Events between", start_date, "and", end_date)
    for event in events_between_dates:
        print(event['summary'])

    # Modify a specific event
    event_id_to_modify = '<event-id-to-modify>'
    new_data = {
        'summary': 'Updated Event',
        'start': {'dateTime': '2023-06-27T16:00:00'},
        'end': {'dateTime': '2023-06-27T17:00:00'}
    }
    modified_event = modify_event(event_id_to_modify, new_data)
    print("Modified event:", modified_event['summary'])
