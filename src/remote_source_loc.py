import boto3
import glob
import logging

def listOfLocalFiles(path):
    try:
        filesList = glob.glob(path + "/*") 
        return filesList
    except Exception as e:
        logging.error(e)

def getListOfS3Buckets():
    try:
        bucketList = []
        s3 = boto3.resource('s3')

        for bucket in s3.buckets.all():
            bucketList.append(bucket.name)
        return bucketList
    except Exception as e:
        print(e)

def uploadToS3() -> bool:
    try:
        return True
    except Exception as e:
        print(e)

def checkS3Buckets(bucket_name):
    try:
        bucketList = getListOfS3Buckets()

        for bucket in bucketList:
            if bucket == bucket_name:
                uploadLoadToS3 = uploadToS3()
                if uploadLoadToS3 == True:
                    print("files loaded")
                else:
                    print("files not loaded")
    except Exception as e:
        print(e)

            

if __name__ == "__main__":

    path = r"C:\\Users\\SambasivaRaoT\\LearningPath\\iNeuron\\DataScience\\DataScience_ML_DL_Masterclass\\DATA"
    bucket_name = "DataScience_ML_DL_Masterclass"