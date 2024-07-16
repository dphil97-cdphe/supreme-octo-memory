"""
TODO
----
- use aiohttp package to download files asynchronously
- use ThreadPoolExecutor in python to download files
- write unit tests
- re-use requests session
- use Pathlib instead of os
- figure out Docker and Docker images

function: download image
  open request
  download file
function: unzip image
function: main
  loop through urls
  make directory if not exists
  check for valid url
  ThreadPoolExecutor here

"""
import os
import zipfile
from concurrent.futures import ThreadPoolExecutor
import requests

urls = [
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
      "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
      ]

def download_file():
   pass

def process_file(fname):
    
   # Create zip file
    with open(fname, 'wb') as f:
      f.write(r.content)

    with zipfile.ZipFile(fname, 'r') as zip_obj:
      zip_obj.extractall()

    os.remove(fname)

def main():

  # Create dir if not exists and move there
  os.makedirs('downloads', exist_ok=True)
  os.chdir("downloads")

  for url in urls:
     
     with ThreadPoolExecutor() as executor:
        executor.map(download_file, urls)

if __name__ == "__main__":
   main()