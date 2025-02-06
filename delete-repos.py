import requests

# Configuration
GITHUB_TOKEN = "your_personal_access_token"  # Replace with your GitHub token
USERNAME = "your_github_username"  # Replace with your GitHub username
REPOS_TO_DELETE = [
    "repo1",  # Replace with the names of the repositories you want to delete
    "repo2",
    "repo3"
]

# GitHub API URL
API_URL = "https://api.github.com"

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def delete_repository(repo_name):
    """Delete a repository by name."""
    url = f"{API_URL}/repos/{USERNAME}/{repo_name}"
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 204:
        print(f"✅ Repository '{repo_name}' deleted successfully.")
    else:
        print(f"❌ Failed to delete repository '{repo_name}'. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

def delete_multiple_repositories(repo_list):
    """Delete multiple repositories."""
    for repo in repo_list:
        delete_repository(repo)

if __name__ == "__main__":
    delete_multiple_repositories(REPOS_TO_DELETE)
