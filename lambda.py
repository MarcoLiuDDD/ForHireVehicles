import boto3
import requests

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    api_url = 'https://data.cityofnewyork.us/resource/8wbx-tsch.json'
    s3_bucket = 'for-hire-vehicles'
    s3_key = 'data/fhv_active_data.json'

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=json.dumps(data))
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

    return {
        'statusCode': 200,
        'body': json.dumps('Data ingested successfully!')
    }