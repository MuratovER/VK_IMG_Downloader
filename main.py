import requests
import json
import random

vk_token: str = {YOUR_VK_TOKEN}
vk_id: int = {YOUR_VK_ID}


def get_photo_info(offset=0, count=100):
    """Get all photos from your vk page"""
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': vk_id,
        'access_token': vk_token,
        'offset': offset,
        'count': count,
        'photo_sizes': 0,
        'no_service_albums': 0,
        'v': 5.131
    })

    return json.loads(api.text)


def size_check(dataframe: dict) -> dict:
    """Filter and save only {y} size photo urls and give them random name """
    if dataframe["type"] == 'y':
        file_url = dataframe["url"]
        photo = {}
        photo["url"] = file_url
        photo['filename'] = random.randint(0, 10000000)
        return photo


def data_parcer(offset: int, count: int) -> dict:
    """Parcing given data and return only filtered"""
    dataframe = []
    data = get_photo_info(offset, count)

    for photo in data["response"]["items"]:
        photo_set = photo["sizes"]
        for element in photo_set:
            photo_info = size_check(element)
            if photo_info is not None:
                dataframe.append(photo_info)
    return dataframe


def file_save(api: requests, filename: str) -> str:
    """Save images"""
    with open("images/%s" % filename + ".jpg", "wb") as file:
        file.write(api.content)
    return "Photo was saved with name" + filename


def get_photo(offset, count):
    """Get photo url and saved them"""
    filtered_data = data_parcer(offset, count)
    for photo in filtered_data:
        api = requests.get(photo["url"])
        file_save(api, photo["filename"])
    return "All photos was saved"


def main():
    """Main program that runs all the code"""
    step = 50
    max_count = get_photo_info(0, 1)["response"]["count"]
    for offset in range(0, max_count+1, step):
        get_photo(offset, step)


if __name__ == '__main__':
    main()
