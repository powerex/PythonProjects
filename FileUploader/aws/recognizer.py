import csv
import boto3


def get_labels(filename):
    with open('../keys/accessKeys.csv', 'r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[0]
            secret_access_key = line[1]

    photo = '../images/'+filename

    client = boto3.client('rekognition',
                          region_name='eu-central-1',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)

    with open(photo, 'rb') as source_image:
        source_bytes = source_image.read()

    response = client.detect_labels(Image={
        'Bytes': source_bytes
    },
        MaxLabels=10,
        MinConfidence=95)

    name_list = {item.get('Name'): '{:5.2f}'.format(item.get('Confidence')) for item in response.get('Labels')}
    print(name_list)

    return name_list
