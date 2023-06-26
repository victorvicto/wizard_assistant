from telegram import *
from g_calendar import *

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
        "name": "add_events_to_calendar",
        "description": "Adds multiple events to the user's google calendar.",
        "parameters": {
            "type": "object",
            "properties": {
                "events": {
                    "type": "list of objects",
                    "description": "A list of google calendar events. Each event should at least contain a summary, a start date and time and an end date and time. Unless specified otherwise, the timezone of each event should be the one of Brussels.",
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
                    "type": "list of strings",
                    "description": "a list of strings. The events returned by the function will be filtered to match the keywords in that list.",
                }
            },
            "required": ["start_date","end_date"],
        },
    },
    {
        "name": "delete_events",
        "description": "Deletes all the user's google calendar events who's ids have been given as an argument.",
        "parameters": {
            "type": "object",
            "properties": {
                "event_ids": {
                    "type": "list of strings",
                    "description": "A list of ids corresponding to the events that should be deleted from the google calendar.",
                }
            },
            "required": ["event_ids"],
        },
    }
]

available_functions = {
    "send_message_to_friends": send_message_to_friends,
    "add_events_to_calendar": add_events_to_calendar,
    "get_events_between_dates": get_events_between_dates,
    "delete_events": delete_events
}

