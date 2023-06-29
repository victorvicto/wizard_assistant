from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from secret_keys import *
from communicating import *
import json

# Authenticate and create a Google Calendar service instance
def authenticate():
    return "cul"
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_current_day():
    return datetime.strftime(datetime.today(), "%y-%m-%d")

service = authenticate()

# Function to add events to a Google Calendar
async def add_events_to_calendar(events):
    conf = await confirm("\nEVENTS TO BE ADDED:"+events+"\n\n")
    if conf:
        #service = authenticate() # not necessary anymore, done in globals but might still come in handy if the authentication cancels automatically
        try:
            for event in events:
                event_body = json.loads(event)
                service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
            return "success"
        except Exception as err:
            return "an error occured: "+err
    return "cancelled by user"

# def add_event_to_calendar(event):
#     # service = authenticate() // not necessary anymore, done in globals but might still come in handy if the authentication cancels automatically
#     # for event in events:
#     #     event_body = {
#     #         'summary': event['summary'],
#     #         'start': {'dateTime': event['start']},
#     #         'end': {'dateTime': event['end']}
#     #     }
#     #     service.events().insert(calendarId=CALENDAR_ID, body=event_body).execute()
#     print("\nEVENTS TO BE ADDED:")
#     print(event)
#     print()
#     return "success"

# Function to retrieve events from a Google Calendar between specified start and end dates
async def get_events_between_dates(start_date, end_date, keywords=None):
    #service = authenticate()
    conf = await confirm("\nPERIOD REQUIRED:\n\tstart: "+start_date+"\n\tend: "+end_date+"\n\tkeywords: "+str(keywords)+"\n")
    if conf:
        try:
            start_datetime = datetime.strptime(start_date, "%y-%m-%d")
            start_datetime.time = datetime.min.time()
            end_datetime = datetime.strptime(end_date, "%y-%m-%d")
            end_datetime.time = datetime.max.time()
            start_datetime_format = start_datetime.isoformat() + 'Z'
            end_datetime_format = end_datetime.isoformat() + 'Z'

            events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=start_datetime_format, timeMax=end_datetime_format,
                                                singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])

            final_list = events
            if keywords is not None:
                filtered_events = []
                for event in events:
                    for k in keywords:
                        if k.lower() in event.get('summary', '').lower():
                            filtered_events.append(event)
                            break
                final_list = filtered_events
            return "{'status': 'success', 'events': '"+str(final_list)+"'}"
        except Exception as err:
            return "{'status': 'an error occured', 'error': '"+err+"'}"
    return "{'status': 'cancelled by user'}"

# Function to modify a specific event in a Google Calendar
async def modify_event(event_id, new_data):
    #service = authenticate()
    conf = await confirm("\nMODIFIED EVENT:\n"+str(new_data)+"\n")
    if conf:
        try:
            event = service.events().get(calendarId=CALENDAR_ID, eventId=event_id).execute()
            event.update(new_data)
            updated_event = service.events().update(calendarId=CALENDAR_ID, eventId=event_id, body=event).execute()
            return "success"
        except Exception as err:
            return "an error occured: "+err
    return "cancelled by user"

async def delete_events(event_ids):
    #service = authenticate()
    conf = await confirm("\nEVENTS TO BE DELETED:\n"+str(event_ids)+"\n")
    if conf:
        try:
            for event_id in event_ids:
                service.events().delete(calendarId=CALENDAR_ID, eventId=event_id).execute()
            return "success"
        except Exception as err:
            return "an error occured: "+err
    return "cancelled by user"

