import pytest
import uuid
from pathlib import Path
from src.minio_client import MinioClientNative
from src.minio_client import MinioClientS3


@pytest.fixture()
def bucket_name() -> str:
    return "test-bucket"


@pytest.fixture()
def minio_client_native(bucket_name: str) -> MinioClientNative:
    return MinioClientNative(bucket_name=bucket_name)


@pytest.fixture()
def minio_client_s3(bucket_name: str) -> MinioClientS3:
    return MinioClientS3(bucket_name=bucket_name)


@pytest.fixture()
def file_to_save(tmp_path: Path) -> Path:
    file_name = f"{uuid.uuid4()}.mock"
    _file_to_save = tmp_path / file_name
    with open(_file_to_save, "a") as f:
        f.write(str(file_name))
    return _file_to_save


class TestMinioClientNative:
    def test_upload_file(self, minio_client_native: MinioClientNative, file_to_save: Path, tmp_path: Path):
        minio_client_native.upload_file(file_to_save)
        # assert ... check file exists on minio
        assert f'{file_to_save.name}' == minio_client_native.get_object(object_name=file_to_save.name)
        
        path_to_save = tmp_path / "saved_file.mock"
        minio_client_native.download_file(object_name=file_to_save.name, file_path=path_to_save)
        # check file exists locally
        assert path_to_save.exists()


class TestMinioClientS3:
    def test_upload_file(self, minio_client_s3: MinioClientS3, file_to_save: Path, tmp_path: Path):
        minio_client_s3.upload_file(file_to_save)
        # assert ... check file exists on minio

        path_to_save = tmp_path / "saved_file.mock"
        minio_client_s3.download_file(object_name=file_to_save.name, file_path=path_to_save)
        # check file exists locally
        assert path_to_save.exists()
