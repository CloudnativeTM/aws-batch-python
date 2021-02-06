import os
import boto3
import zipfile
import io
import csv
from botocore.exceptions import ClientError

if __name__ == '__main__':


    # Start process
    print("Starting ZiptoCatalog")
    bucket = os.getenv('MY_BUCKET')
    key = os.getenv('MY_KEY')
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    dynamodb = boto3.ressource('dynamodb')

    print(bucket)
    print(key)


    print(key.split('.')[0])
    userId = key.split('.')[0]

    

    zip_obj = s3.Object(bucket, key)
    buffer = io.BytesIO(zip_obj.get()["Body"].read())
    z = zipfile.ZipFile(buffer)

    
    for filename in z.namelist():
        print(z.getinfo(filename))
    
    z.extractall('')

    #test files, check csv, format testing, ; --> , 

    #get id out of csv name and delete all data in dynamoDB
    table = dynamodb.Table('products')
    with table.batch_writer() as scan:
        while scan is None or 'LastEvaluatedKey' in scan:
            if scan is not None and 'LastEvaluatedKey' in scan:
                scan = table.scan(
                    ProjectionExpression='userId',
                    ExclusiveStartKey=scan['LastEvaluatedKey'],  
                )
            else:
                scan = table.scan(ProjectionExpression='userId')
            for item in scan['Items']:
                batch.delete_item(Key={
                    'userId' : item[userId]
                })


    with open('products.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for rows in reader:
            print(rows)
            print('productName')
            print(rows['sku'])

            try:
                response = s3_client.upload_file(rows['image'], "productimagesportle", "public/"+rows['image'])
                

                #Post dynamo Object with userId




            except ClientError as er:
                print(er)
                
    
    print("Completed run...")
