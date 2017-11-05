import boto3
import os
from boto3.s3.transfer import S3Transfer

def get_transfer():
    client = boto3.client('s3')
    return S3Transfer(client, None)

def download_file(bucket, key, local_path):
    t = get_transfer()
    t.download_file(bucket, key, local_path)

def download_files(bucket, files, folder_path):
	if not files:
		raise Exception('list cannot be empty')

	for file in files:
		file_name = os.path.basename(file)
		file_final_path = os.path.join(folder_path, file_name)

		download_file(bucket, file, file_final_path)
