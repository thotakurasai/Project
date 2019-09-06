import boto3

bucketName = "test-bucket-saikiran"
Key = "Req.txt"
outPutname = "Require"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)
