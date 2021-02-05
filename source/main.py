import os
import boto3
import zipfile
import BytesIO







if __name__ == '__main__':


    # Start process
    print("Starting ZiptoCatalog")
    bucket = os.getenv('MY_BUCKET')
    key = os.getenv('MY_KEY')


    print(bucket)
    print(key)

    s3 = boto3.resource('s3')
    zip_obj = s3.Object(bucket, key)


    buffer = BytesIO(zip_obj.get()["Body"].read())

    z = zipfile.ZipFile(buffer)
    for filename in z.namelist():
        print(z.getinfo(filename))
 



    print("Completed run...")
