from django.contrib import admin
from django.urls import path,include
from . import upload_audio,transcribe
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('getUploadAudio', upload_audio.getUploadAudio),
    path('getTranscribe', transcribe.getTranscribe),
]
