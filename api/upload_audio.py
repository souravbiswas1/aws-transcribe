#Importing libraries---
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
# import array
import s3fs
from requests.auth import HTTPBasicAuth
from boto.s3.connection import S3Connection, Bucket, Key
import boto3
import urllib.request
from api.config import access_key_id
from api.config import secret_access_key
from api.config import s3_bucket_name
from api.config import s3_region
from api.config import s3_key
# from api.config import audio_path

@api_view(['POST'])
def getUploadAudio(request):
    def upload_audio(URL):
        ACCESS_KEY_ID = access_key_id()
        SECRET_ACCESS_KEY = secret_access_key()
        bucket_name = s3_bucket_name()
        region = s3_region()
        keyname = s3_key()
        file_name = URL.split('/')[-1]
        urllib.request.urlopen(URL).read()
        s3 = boto3.client('s3', region_name = region, aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
        s3.upload_file(file_name, bucket_name, keyname.format(file_name))
        key = ['Message']
        val = [file_name + ' uploaded']
        keyval = dict(zip(key,val))
        return keyval

    if request.method == "POST":
        try:
            respAudio = upload_audio(request.data['url'])
            return Response(respAudio)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response("Error in upload_image response",status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Error in POST response",status=status.HTTP_400_BAD_REQUEST)
