from concurrent.futures import ThreadPoolExecutor
import urllib.request
import zipfile
import os

DOWNLOAD_DIR = 'downloads'

URLS = [
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
      ]

def process_file(url):

    # Point to download directory
    destination_folder = os.path.join(os.getcwd(), DOWNLOAD_DIR)

    # Get file name from url
    zip_filename = os.path.basename(url)

    # Final destination path requires filename
    destination_path = os.path.join(destination_folder, zip_filename)

    try:
        # Download file
        urllib.request.urlretrieve(url, destination_path)
        print(f"{zip_filename} retrieved from {url}\n")
    except urllib.error.HTTPError as e :
        print(f"HTTPError: {url} {e.reason}")

    # TODO
    # unzip file
    # delete original .zip file

def main():

    # Create directory and move to it for downloading
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for url in URLS:
        process_file(url)


if __name__ == "__main__":
    main()


