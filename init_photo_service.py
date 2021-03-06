import os
from Google import Create_Service
import pandas

API_NAME= 'photoslibrary'
API_VERSION= 'v2'
CLIENT_SECRET_FILE= 'client_secret_frame.json'
SCOPES= ['https://www.googleapis.com/auth/photoslibrary',
'https://www.googleapis.com/auth/photoslibrary.sharing']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)