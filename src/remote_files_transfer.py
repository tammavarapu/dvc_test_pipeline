import boto3
import os
import logging
import glob

from botocore.exceptions import ClientError

class RemoteSource:

    def __init__(self):
        self.resource = boto3.resource('s3')
        self.bucketList = []
        self.path = r"C:\\Users\\SambasivaRaoT\\LearningPath\\iNeuron\\DataScience\\DataScience_ML_DL_Masterclass\\DATA"
        self.bucket_name = "datascience-ml-dl-masterclass"
        self.args = {'ACL': 'public-read'}

    def localFiles(self):
        localFiles = glob.glob(self.path + "/*")
        return localFiles

    def listOfBuckets(self):

        try:        
            for bucket in self.resource.buckets.all():
                self.bucketList.append(bucket.name)
        except ClientError as ce:
            logging.error(ce)

        return self.bucketList

    def create_bucket(self,bucket_name,data):
        """
        
        """
        try:
            bucketList = self.listOfBuckets()
            for bucket in bucketList:
                if bucket == self.bucket_name:
                    #self.resource.create_bucket(Bucket=self.bucket_name)
                    self.resource.Bucket(self.bucket_name).put_object(data)
                    print(f"s3 {bucket} created")

            #self.client.create_bucket(Bucket=bucket_name)
        except ClientError as ce:
            logging.error(ce)
            return False

        return True

    def upload_files(self):
        files = self.localFiles()

        for file in files:
            f = file.split("\\")
            data = f[-2]
            file = f[-1]
            self.create_bucket(self.bucket_name, data)
            self.resource.Object(self.bucket_name, file).upload_file(Filename=file)

    def s3FilesList(self):
        with open('s3_bucket_files.txt','w') as f:
            pass

    
            


if __name__ == "__main__":
    remote = RemoteSource()
    remote.upload_files()



