import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from botocore.exceptions import ClientError


class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file_path: str,
    ):
        object_name = file_path.split("/")[-1]
        try:
            async with self.get_client() as client:
                with open(file_path, "rb") as file:
                    await client.put_object(
                        Bucket=self.bucket_name,
                        Key=object_name,
                        Body=file,
                    )
                print(f"File {object_name} uploaded to {self.bucket_name}")
        except ClientError as e:
            print(f"Error uploading file: {e}")

    async def delete_file(self, object_name: str):
        try:
            async with self.get_client() as client:
                await client.delete_object(Bucket=self.bucket_name,
                                           Key=object_name)
                print(f"File {object_name} deleted from {self.bucket_name}")
        except ClientError as e:
            print(f"Error deleting file: {e}")

    async def get_file(self, object_name: str, destination_path: str):
        try:
            async with self.get_client() as client:
                response = await client.get_object(Bucket=self.bucket_name,
                                                   Key=object_name)
                data = await response["Body"].read()
                with open(destination_path, "wb") as file:
                    file.write(data)
                print(f"File {object_name} downloaded to {destination_path}")
        except ClientError as e:
            print(f"Error downloading file: {e}")


async def main():
    s3_client = S3Client(
        access_key="e6e12b1688eb4963be8ed00f1631d681",
        secret_key="0f726d9dbd294cc59787535fc9eb4eb8",
        endpoint_url="https://s3.storage.selcloud.ru",
        bucket_name="memes-cont-1"
    )

    await s3_client.upload_file("meme.jpg")
    await s3_client.upload_file("mem1.jpg")
    await s3_client.upload_file("10guy.jpg")
    await s3_client.upload_file("advice_dog.jpg")
    await s3_client.upload_file("bear_grylls.jpg")
    await s3_client.upload_file("brace_yourselves_x_is_coming.jpg")
    await s3_client.upload_file("cat_gasp.jpg")
    await s3_client.upload_file("chemistry_cat.jpg")
    await s3_client.upload_file("conspiracy_keanu.jpg")
    await s3_client.upload_file("depression_dog.jpg")
    await s3_client.upload_file("disaster_girl.jpg")
    await s3_client.upload_file("evil_cows.jpg")
    await s3_client.upload_file("foul_bachelor_frog.jpg")
    await s3_client.upload_file("hipster_kitty.jpg")

if __name__ == "__main__":
    asyncio.run(main())
