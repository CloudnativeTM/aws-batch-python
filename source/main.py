import os
import boto3
import zipfile
import io
import csv

from awsS3Io import AwsS3Io
from sampleProcess import SampleProcess





if __name__ == '__main__':


    # Start process
    print("Starting ZiptoCatalog")
    bucket = os.getenv('MY_BUCKET')
    key = os.getenv('MY_KEY')


    print(bucket)
    print(key)

    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, key)

    with io.BytesIO(obj.get()["Body"].read()) as tf:

    # rewind the file
    tf.seek(0)

    # Read the file as a zipfile and process the members
    with zipfile.ZipFile(tf, mode='r') as zipf:
        zip_ref.extractall('')

    with open('addresses.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)



    print("Completed run...")
