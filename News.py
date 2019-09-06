import requests
import boto3

url = ('https://newsapi.org/v2/everything?'
       'q=Steve Smith&'
       'sources=bbc-news,the-hindu,abc-news&'
       'from=2019-09-05&'
       'sortBy=popularity&'
       'apiKey=5579350968fb43f6861a0db1b887235c')

response = requests.get(url)

t="Newsoutputs.txt"

f = open(t,"a")
print(response.json(),file=f)
f.close()

bucketName = "test-bucket-saikiran"
Key = t
outPutname = t

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)



"""response.json()

directory_name = "aniket/bucket/python" #it's name of your folders
s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
"""

