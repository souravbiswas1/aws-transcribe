
import requests
from requests.auth import HTTPBasicAuth

def access_key_id():
	ACCESS_KEY_ID = 'XXXXXXXXXXXXXXXXXXXXXXX'
	return ACCESS_KEY_ID

def secret_access_key():
	SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	return SECRET_ACCESS_KEY

def s3_bucket_name():
	bucket = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
	return bucket

def s3_region():
	s3Region = 'XXXXXXXXXXXXXXXXX'
	return s3Region

def s3_key():
	key = 'XXXXXXXX/{}'
	return key
