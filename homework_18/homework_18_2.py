import requests

# POST
with open('test.jpg', 'rb') as img_file:
    files = {
        'image': ('homework_18.jpg', img_file, 'image/*')
    }
    response = requests.post('http://127.0.0.1:8080/upload', files=files)

if response.status_code == 201:
    created_img = response.json()['image_url']
    print('Uploaded image path:', created_img)
else:
    print('Error status code:', response.status_code)

# GET
url = 'http://127.0.0.1:8080/image/homework_18.jpg'
header = {'User-Agent': 'Homework', 'Content-Type': 'text'}

response = requests.get(url, headers=header)
if response.status_code == 200:
    data = response.json()['image_url']
    print(data)
else:
    print('Request Error:', response.status_code)

# DELETE
url = 'http://127.0.0.1:8080/delete/homework_18.jpg'
response = requests.delete(url)

if response.status_code == 200:
    print('Data successfully deleted')
else:
    print('Error status code:', response.status_code)


