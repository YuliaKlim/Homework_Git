import requests

base_url = 'https://images-api.nasa.gov'

# Image search
search_url = f'{base_url}/search'
search_params = {
    'q': 'Curiosity rover Mars',
    'media_type': 'image',
    'page_size': 20
}

response = requests.get(search_url, params=search_params)
#print(response.json())
items = response.json()['collection']['items']

# Getting files by nasa_id
asset_url_template = f'{base_url}/asset/{{nasa_id}}'

# Processing of the first two finds
for i in range(2):
    # Take nasa_id
    nasa_id = items[i]['data'][0]['nasa_id']

    # Getting urls to files
    asset_res = requests.get(asset_url_template.format(nasa_id=nasa_id))
    #print(asset_url_template.format(nasa_id=nasa_id))
    #print(asset_res.json())

    # Take the 'href' of the first object in the items list
    img_url = asset_res.json()['collection']['items'][0]['href']

    # Download
    img_data = requests.get(img_url).content
    with open(f'mars_photo{i + 1}.jpg', 'wb') as f:
        f.write(img_data)
    print(f'mars_photo{i + 1}.jpg ready!')