import csv
import boto3

with open('../keys/accessKeys.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[0]
        secret_access_key = line[1]

print(secret_access_key)

client = boto3.client('rekognition',
                      region_name='eu-central-1',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key)

response = client.detect_faces(Image={'S3Object': {
    'Bucket': 'rekonize',
    'Name': 'faces/Chad.jpg'
}},
    Attributes=['ALL']
)

print(response)
