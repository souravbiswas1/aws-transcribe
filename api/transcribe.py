#Importing libraries---
from __future__ import print_function
import pandas as pd
import numpy as np
import json
# from bson import json_util
from django.shortcuts import render
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
import pickle
import requests
import sys
import os
import array
import s3fs
from requests.auth import HTTPBasicAuth
from boto.s3.connection import S3Connection, Bucket, Key
import boto3
import time
import urllib
from api.config import access_key_id
from api.config import secret_access_key
from api.config import s3_bucket_name
from api.config import s3_region

@api_view(['POST'])
def getTranscribe(request):
    def speech_recognition(job,url):
        ACCESS_KEY_ID = access_key_id()
        SECRET_ACCESS_KEY = secret_access_key()
        bucket_name = s3_bucket_name()
        region = s3_region()
        transcribe = boto3.client('transcribe', region_name = region, aws_access_key_id = ACCESS_KEY_ID, aws_secret_access_key = SECRET_ACCESS_KEY)
        job_name = str(job)
        job_uri = str(url)
        path = urllib.parse.urlparse(url).path
        ext = os.path.splitext(path)[1].lstrip('.')
        transcribe.start_transcription_job(
            OutputBucketName = bucket_name,
            TranscriptionJobName = job_name,
            Media = {'MediaFileUri': job_uri},
            MediaFormat = ext,
            LanguageCode = 'en-US'
        )
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            print("Not ready yet...")
            time.sleep(5)
        return status

    if request.method == "POST":
        try:
            resp = speech_recognition(request.data['job'],request.data['url'])
            return Response(resp)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response("Error in speech_recognition response",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Error in POST response",status=status.HTTP_400_BAD_REQUEST)
