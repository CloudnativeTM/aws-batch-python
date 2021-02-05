import os
import boto3
import zipfile
import io
import csv








if __name__ == '__main__':


    # Start process
    print("Starting ZiptoCatalog")
    bucket = os.getenv('MY_BUCKET')
    key = os.getenv('MY_KEY')


    print(bucket)
    print(key)

    s3 = boto3.resource('s3')
    zip_obj = s3.Object(bucket, key)


    buffer = io.BytesIO(zip_obj.get()["Body"].read())

    z = zipfile.ZipFile(buffer)

    
    for filename in z.namelist():
        print(z.getinfo(filename))
    
    z.extractall('')
    
    
    data={}
    with open('products.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for rows in reader:
            print(rows)
            print(rows['sku'])


    

    
    print("Completed run...")
