import requests

BASE_URL = "http://10.100.20.51:8000/"

ENDPOINT = "api/Meeting/GetMeetings"

def get_meetings():
    meeting = requests.get(BASE_URL + ENDPOINT)
    meetings =meeting.json()
    
    if meeting.status_code == 200:
        print('request successful!!')
    else:
        print('you know wetin you dey do so?')
    return meetings

print(get_meetings())