import logging
import sys
import os

from awsS3Io import AwsS3Io
from sampleProcess import SampleProcess


def run(output_dir, s3destination):
    downloaded_file = SampleProcess().run(output_dir)
    # If s3 uri is present upload to s3
    if s3destination is not None:
        AwsS3Io().uploadfile(downloaded_file, s3destination)


if __name__ == '__main__':



    # Start process
    logger.info("Starting ZiptoCatalog")
    name = os.getenv('MY_BUCKET')
    value = os.egetenv('MY_KEY')


    logger.info(name)
    logger.info(value)

    logger.info("Completed run...")
