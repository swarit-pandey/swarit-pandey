import requests

# Meme API endpoint
API_URL = "https://meme-api.com/gimme"


def fetch_random_meme():
    response = requests.get(API_URL)
    if response.status_code == 200:
        meme_url = response.json().get('url')  # The URL of the meme image
        return meme_url
    else:
        print("skill-issue :", response.status_code)
        return None


def update_readme(meme_url):
    readme_contents = f"""
# My GitHub Profile

Welcome to my GitHub profile! Enjoy a random meme every day:

![Random Meme]({meme_url})

Feel free to check out my projects below.
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_contents)


if __name__ == "__main__":
    meme_url = fetch_random_meme()
    if meme_url:
        update_readme(meme_url)
