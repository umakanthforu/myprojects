import boto3

## ACCESS KEYS
ak = 'AKIATEYN5PTWUBCB2MMC'
sak = '1BO6iOP0sHgYd5cWV8T9zZVZ3FHWq/sptIc96aTm'

## DEFINING CLIENT
s3_client = boto3.client(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id=ak,
    aws_secret_access_key=sak,
)

response = s3_client.put_object(
    Body="s3upload.txt",
    Bucket='aws-s3-umakanth-achukolu',
    Key='s3upload.txt',
)
