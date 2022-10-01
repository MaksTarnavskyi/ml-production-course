from pathlib import Path
import s3fs
from minio import Minio

ACCESS_KEY = "minio"
SECRET_KEY = "minio123"
ENDPOINT = "127.0.0.1:9000"

class MinioClientNative:
    def __init__(self, bucket_name: str) -> None:
        client = Minio(ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

        self.client = client
        self.bucket_name = bucket_name

        if not self.check_bucket_exist():
            self.create_new_bucket()
        
    def check_bucket_exist(self):
        return self.client.bucket_exists(self.bucket_name)

    def create_new_bucket(self):
        return self.client.make_bucket(self.bucket_name)

    def upload_file(self, file_path: Path):
        self.client.fput_object(self.bucket_name, file_path.name, file_path)

    def get_object(self, object_name: str):
        response = self.client.get_object(self.bucket_name, object_name)
        object = response.data.decode()
        return object
    
    def download_file(self, object_name: str, file_path: Path):
        self.client.fget_object(bucket_name=self.bucket_name, object_name=object_name, file_path=str(file_path))

    def delete_file(self, object_name: str):
        self.client.remove_object(bucket_name=self.bucket_name, object_name=object_name)

    def delete_bucket(self):
        self.client.remove_bucket(bucket_name=self.bucket_name)


class MinioClientS3:
    def __init__(self, bucket_name: str) -> None:

        fs = s3fs.S3FileSystem(
            key=ACCESS_KEY, secret=SECRET_KEY, use_ssl=False, client_kwargs={"endpoint_url": f"http://{ENDPOINT}"}
        )

        self.client = fs
        self.bucket_name = bucket_name

    def get_s3_file_path(self, object_name: str):
        s3_file_path = f"s3://{self.bucket_name}/{object_name}"
        return s3_file_path

    def upload_file(self, file_path: Path):
        s3_file_path = self.get_s3_file_path(file_path.name)
        self.client.put(str(file_path), s3_file_path)

    def download_file(self, object_name: Path, file_path: Path):
        s3_file_path = self.get_s3_file_path(object_name)
        self.client.download(s3_file_path, str(file_path))

    def delete_file(self, object_name: Path):
        s3_file_path = self.get_s3_file_path(object_name)
        self.client.delete(s3_file_path)

