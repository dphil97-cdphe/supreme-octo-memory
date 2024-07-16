from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import time
import os

# Downloads image from URL and saves it locally
def download_image(url):
    
    image_data = None
    with urlopen(url) as f:
        image_data = f.read()

    try:
        filename = os.path.basename(url)
        with open(filename, 'wb') as image_file:
            image_file.write(image_data)
            print(f"{filename} was downloaded.")

    except Exception:
        raise Exception(f"Could not download from {url}")

def main():
    urls = [
        'https://upload.wikimedia.org/wikipedia/commons/9/9d/Python_bivittatus_1701.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/4/48/Python_Regius.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/d/d3/Baby_carpet_python_caudal_luring.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/f0/Rock_python_pratik.JPG',
        'https://upload.wikimedia.org/wikipedia/commons/0/07/Dulip_Wilpattu_Python1.jpg']

    
    os.makedirs("images", exist_ok=True)

    os.chdir("images")

    print(os.getcwd())

    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

if __name__ == "__main__":
    main()