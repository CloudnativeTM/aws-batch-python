import argparse
import logging
import sys

from awsS3Io import AwsS3Io
from sampleProcess import SampleProcess


def run(output_dir, s3destination):
    downloaded_file = SampleProcess().run(output_dir)
    # If s3 uri is present upload to s3
    if s3destination is not None:
        AwsS3Io().uploadfile(downloaded_file, s3destination)


if __name__ == '__main__':

    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Start process
    logger.info("Starting run with arguments...")

    logger.info("Hello World!")

    logger.info("Completed run...")
