import aws_cdk.aws_s3 as s3
from aws_cdk.aws_iam import PolicyStatement
from aws_cdk.aws_lambda import (
    Code,
    Function
)
from aws_cdk import Duration, Stack


class YtConvertorStack:
    def __init__(self, stack: Stack):
        bucket = s3.Bucket(
            scope=stack,
            id='yt_video_storage'
        )

        yt_lambda = Function(
            scope=stack,
            id='yt_convertor_lambda',
            code=Code.from_asset(path='handlers/yt_convertor_lambda'),
            handler='handler',
            timeout=Duration.minutes(15),
            environment={
                'BUCKET_NAME': bucket.bucket_name
            },
            initial_policy=[
                PolicyStatement(
                    actions=["s3:UploadFile"],
                    resources=[bucket.bucket_arn]
                )
            ]
        )

