# I used the NASA API, specifically the APOD(Astronomy picture of the day) API
# This API's documentation was moved to a wordpress site, so I reviewed details at
# https://schlotterer.notion.site/APOD-Feed-And-API-User-Guide-39697d8747c38015a53edfdde76d4f5e
# Also realized several hours in that this API will not allow json to be returned, so I had
# to use xml and got some help from forums to figure out the syntax for those structures

# Call the API with Postman
"""
For this section, I sent a GET request to see the data for february 2014. I selected GET,
entered the site https://science.nasa.gov/feed/apod-basic/ with the params for year and month 
added as ?year=2014&month=2. This returned a ton of information including a link to view the image,
a description of what is happening in the photo, the date, the owner of the image, and the title.
"""

# Call the API with Python
import requests
import time
# Added this import because this particular API does not return json
import xml.etree.ElementTree as ET

# List of specific months I want data for
months = [
    "4",
    "11",
]

# Make requests for all months in the dates list
for month in months:
    response = requests.get(
        "https://science.nasa.gov/feed/apod-basic/",
        params={
            "year": 2024,
            "month": month,
            "format": "json"
        }
    )

    xml_response = ET.fromstring(response.text) 
    
    # NASA uses "apod" for some of its XML fields 
    namespace = { "apod": "https://science.nasa.gov/apod/" } 
    
    # Iterates through each apod in the list
    for item in xml_response.findall(".//item"): 
        title = item.findtext("title") 
        image_url = item.findtext("apod:hdurl", namespaces=namespace) 
        description = item.findtext("apod:explanation", namespaces=namespace) 


    # To keep the responses short, I just wanted the title, image url, and descriptions    
    print("Title:", title) 
    print("Image URL:", image_url) 
    print("Description:", description) 
    print() 
    
    time.sleep(0.25)
  