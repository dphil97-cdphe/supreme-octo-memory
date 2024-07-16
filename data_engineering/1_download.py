"""
TODO
----
- use aiohttp package to download files asynchronously
- use ThreadPoolExecutor in python to doenload files
- write unit tests
- re-use requests session
- use Pathlib instead of os
- figure out Docker and Docker images
"""

import os
import zipfile
import requests as re

urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
    ]

for url in urls:
  with re.get(url, stream=True) as r:
    try:
      r.raise_for_status()
    except Exception as err:
      print(f"Error for file {url}: {err}")

# Make DONWLOAD directory and cd
os.makedirs("downloads", exist_ok=True)

os.chdir("downloads")

os.getcwd()

for url in urls:
  try:
    fname = url.split(('/'))[-1]
    r = re.get(url)

    # Create zip file
    with open(fname, 'wb') as f:
      f.write(r.content)

    with zipfile.ZipFile(fname, 'r') as zip_obj:
      zip_obj.extractall()

  except Exception as err:
    print(f"Error for file {url}: {err}")

    os.remove(fname)