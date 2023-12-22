import os
import requests
from bs4 import BeautifulSoup

# Directory where the images will be saved
save_dir = "images/"

# Create the directory if it does not exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# User-Agent header to mimic a real browser 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# Search query for Google Images
query = "Sujeet Amberkar"

# Constructing the URL for the GET request
url = f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M"

# Sending the GET request
response = requests.get(url, headers=headers)

# Parsing the page source into a BeautifulSoup object
soup = BeautifulSoup(response.content ,'html.parser')

# Find all image tags on the page
images_tags = soup.find_all("img")

# Remove the first image (usually a Google logo or irrelevant image)
del images_tags[0]

# Iterate through each image tag
for i, img in enumerate(images_tags):
    image_url = img['src']

    # Send a GET request to the image URL
    image_data = requests.get(image_url).content

    # Save the image data to a file
    with open(os.path.join(save_dir, f"{query}_{i}.jpg"), "wb") as f:
        f.write(image_data)
