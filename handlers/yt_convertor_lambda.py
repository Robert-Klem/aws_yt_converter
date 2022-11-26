from pytube import YouTube
import boto3
import os


def download(link, file_name):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download(filename=file_name)
        return f'./{file_name}'
    except:
        print("An error has occurred")
    print("Download is completed successfully")


def handler(event, context):
    link = event['link']
    file_name = event['file_name']
    bucket_name = os.getenv('BUCKET_NAME', 'yt_video_storage')
    file_path = download(link, file_name)
    if file_path:
        s3 = boto3.resource('s3')
        s3.Bucket(bucket_name).upload_file(filename=file_path, keystore='Please set keystore')
    else:
        raise BaseException
