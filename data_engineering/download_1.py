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

    # Make destination folder to hold ZIP and member files
    destination_folder = os.path.join(os.getcwd(), DOWNLOAD_DIR)

    # Get ZIP file name from url
    zip_filename = os.path.basename(url)

    # Point to where ZIP file will be saved (incl filename)
    destination_filename = os.path.join(destination_folder, zip_filename)

    try:
        # Download file
        urllib.request.urlretrieve(url, destination_filename)

        # Extract all members of zip file
        with zipfile.ZipFile(destination_filename, mode="r") as archive:
            archive.extractall(destination_folder)

        os.remove(destination_filename)
    
    except Exception as e:
        print(f"{e}")


def main():

    # Create directory for urllib
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        executor.map(process_file, URLS) 


if __name__ == "__main__":
    main()


