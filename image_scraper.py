import requests
from bs4 import BeautifulSoup
import os

def download_images(url, save_folder):
    # Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags in the HTML
        img_tags = soup.find_all('img')

        # Download each image
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                # Get the image file name
                img_name = os.path.join(save_folder, os.path.basename(img_url))

                # Download and save the image
                img_data = requests.get(img_url).content
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)

                print(f"Image saved: {img_name}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage
website_url = 'https://example.com'
save_directory = 'downloaded_images'

download_images(website_url, save_directory)
