import requests
import re
from bs4 import BeautifulSoup


# Set the target URL
url = "http://webstreamer43.autoremarketers.com:8081/?action=stat"

# Send a GET request and handle potential errors
try:
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for unsuccessful requests
except requests.exceptions.RequestException as e:
  print(f"Error: {e}")
  exit()

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
all_text = soup.get_text(separator='\n')

# Define a function to extract the number after the equal sign
def extract_number(text):
    match = re.search(r"(?<=%s=)\d+" % text, all_text, re.IGNORECASE)
    if match:
        return match.group(0)
    else:
        return None

# Keywords list
keywords = ["streams_websocket_out", "streams_rtsp_in"]

# Extract numbers for each keyword
for keyword in keywords:
    number = extract_number(keyword)
    if number:
        print(f'{keyword}: {number}')