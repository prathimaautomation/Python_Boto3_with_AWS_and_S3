# Python Boto3 with AWS and S3
![](python_boto3_aws.png)
### Create an ec2 instance(ubuntu 16.04) eng89_prathima_pythonboto3 on AWS

#### First install Ubuntu software properties package
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
```
#### finally, run the commands below to install Python 3.9
```
sudo apt-get update
sudo apt-get install python3.9
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --config python3
alias python=python3
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
```
#### Installing AWSCLI and boto3
```
sudo pip3 install awscli
sudo pip3 install boto3
OR
pip install awscli
pip install boto3
```
#### Connecting to AWS
aws configure #provide secret keys & region
```
AWS Access Key ID [None]: <enter key ID>
AWS Secret Access Key [None]: <enter access key>
Default region name [None]: eu-west-1
Default output format [None]: json
aws s3 ls
```
#### Creating a boto3 Script
```
#create a python file create_bucket.py
sudo nano create_bucket.py
import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
            CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


bucket_name=input("Bucket name: ")
region=input("Bucket region: ")
create_bucket(bucket_name, region)
```
### List Existing Buckets
- Create python file (list_buckets.py) and add:
```python
import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```
- This should list all the available buckets, you can check to see if you have successfully created one

### Upload Files
- Create python file (upload_file.py) and add:

- (Create a new .txt file, if you dont have anything in your bucket to send)
```python
import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

file_name=input("Name of file you would like to upload: ")
bucket=input("Name of bucket to upload to: ")
upload_file(file_name, bucket)
```
### Download Files from bucket
- This retrieves any file from your bucket to your instance
- Create python file (download_file.py) and add:
```python
import boto3

s3 = boto3.client('s3')

BUCKET_NAME=input("What is the name of the bucket you want to rerieve: ")
FILE_NAME=input("What is the name of the file you want to retrieve: ")
OBJECT_NAME=FILE_NAME

s3.download_file(BUCKET_NAME, OBJECT_NAME, FILE_NAME)
```
```
ubuntu@ip-172-31-19-28:~$ python download_file.py
What is the name of the bucket you want to rerieve: eng89-prathima-boto3
What is the name of the file you want to retrieve: test.txt
```
### Delete Bucket

* Your bucket has to be empty in order to delete it
* To delete files inside bucket, run in termianl aws s3 rm s3://name_of_bucket/name_of_object

- Create python file (delete_bucket.py) and add:
```python
import boto3

s3 = boto3.client('s3')

bucket=input("What is the name of the bucket you would like to delete: ")

response = s3.delete_bucket(Bucket=bucket)
```
* You can check to see if your bucket is removed by running the List Existing Buckets python code above
![](python_boto3.png)