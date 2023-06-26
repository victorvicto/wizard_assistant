from telegram_manager import *
from calendar_manager import *

gpt_functions = [
    {
        "name": "send_message_to_friends",
        "description": "Sends a message to the user's friends via a group chat. This goup chat's members are the user and his friends. The message will look like it has been sent by a bot called \"Vic's wizzard assistant\".",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The message that should be sent to the group chat.",
                }
            },
            "required": ["message"],
        },
    },
    {
        "name": "get_current_day",
        "description": "Returns the current date in the 'year-month-day' format.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "add_events_to_calendar",
        "description": "Adds one or multiple events to the user's google calendar.",
        "parameters": {
            "type": "object",
            "properties": {
                "events": {
                    "type": "array",
                    "items":{
                        "type": "string"
                    },
                    "description": "A list of strings describing events to add to the calendar. The strings must be in json format and follow the google calendar api event structure",
                }
            },
            "required": ["events"],
        },
    },
    {
        "name": "get_events_between_dates",
        "description": "Function that returns a list of the user's google calendar events that take place between a starting date and an end date. The function can also take an argument called keywords. The events returned will be filtered to only contain events who's summary matches the keywords.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "a date string following the 'year-month-day' format. This date corresponds to the beginning of the period of interest.",
                },
                "end_date": {
                    "type": "string",
                    "description": "a date string following the 'year-month-day' format. This date corresponds to the end of the period of interest.",
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "a list of strings. Each string should be a single word. The events returned by the function will be filtered to match the keywords in that list.",
                }
            },
            "required": ["start_date","end_date"],
        },
    },
    {
        "name": "modify_event",
        "description": "Modifies an event in the user's google calendar.",
        "parameters": {
            "type": "object",
            "properties": {
                "event_id": {
                    "type": "string",
                    "description": "The id of the event that should be modified.",
                },
                "new_data":{
                    "type": "string",
                    "description": "A string describing the full modified event. Complete, including the unchanged parameters. The strings must be in json format and follow the google calendar api event structure",
                }
            },
            "required": ["event_id","new_data"],
        },
    },
    {
        "name": "delete_events",
        "description": "Deletes all the user's google calendar events who's ids have been given as an argument.",
        "parameters": {
            "type": "object",
            "properties": {
                "event_ids": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A list of ids corresponding to the events that should be deleted from the google calendar.",
                }
            },
            "required": ["event_ids"],
        },
    }
]

available_functions = {
    "send_message_to_friends": send_message_to_friends,
    "get_current_day": get_current_day,
    "add_events_to_calendar": add_events_to_calendar,
    "get_events_between_dates": get_events_between_dates,
    "modify_event": modify_event,
    "delete_events": delete_events
}

is_async = {
    "send_message_to_friends": True,
    "get_current_day": False,
    "add_events_to_calendar": False,
    "get_events_between_dates": False,
    "modify_event": False,
    "delete_events": False
}

