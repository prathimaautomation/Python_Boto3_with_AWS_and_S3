import boto3

s3 = boto3.resource('s3')
s3.create_bucket(Bucket='eng89prathima-boto3', CreateBucketConfiguration= {'LocattionConstraint': 'eu-west-1'} )

s3_client = boto3.client('s3')
s3.upload_file("images/bat.jpg", "eng89prathima-boto3", "test.png")
s3.download_file("eng89prathima-boto3", "bat.jpg", "images/test.png")

s3.Bucket("eng89prathima-boto3").bucket.objects.all().delete()