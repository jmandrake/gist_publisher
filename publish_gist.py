import requests

url = "https://api.github.com/gists"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
    "X-GitHub-Api-Version": "2022-11-28"
}
data = {
    "description": "Example of a gist",
    "public": False,
    "files": {
        "README.md": {
            "content": "Hello World"
        }
    }
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Gist created successfully!")
    gist_url = response.json()["html_url"]
    print("Gist URL:", gist_url)
else:
    print("Failed to create the gist. Error:", response.text)
