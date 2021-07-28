# Python Boto3 with AWS and S3

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
#create a boto_test.py
sudo nano boto_test.py
import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```
#### boto3 Commands
- Create a Bucket
```
s3_client=boto3.client('s3')
s3_client.create_bucket(Bucket='bucket1')
```
- Upload a file
```
s3_client= boto3.client('s3')
s3_client.upload_file(file_name, bucket, object_name)
```
-Download a file
```
s3=boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
