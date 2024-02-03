import requests

# Meme API endpoint
API_URL = "https://meme-api.com/gimme"

def fetch_random_meme():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if data.get('nsfw'):
            print("NSFW meme skipped")
            return "skill-issue.gif", False 
        else:
            meme_url = data.get('url')  
            return meme_url, True
    else:
        print("skill-issue :", response.status_code)
        return "skill-issue.gif", False  
        
def update_readme(meme_url, is_direct_url):
    if is_direct_url:
        meme_markdown = f"![Random Meme]({meme_url})"
    else:
        meme_markdown = f"![Skill Issue]({meme_url})"
    
    readme_contents = f"""
enjoy a random meme from reddit (updated by gh bot)

{meme_markdown}
"""

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_contents)

if __name__ == "__main__":
    meme_url, is_direct_url = fetch_random_meme()
    update_readme(meme_url, is_direct_url)
