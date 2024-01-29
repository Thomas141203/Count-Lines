import requests

def get_repositories(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    repositories = response.json()
    return [repo["full_name"] for repo in repositories]

def count_lines_of_code(repo_full_name, token):
    url = f"https://api.github.com/repos/{repo_full_name}/contents"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    files = response.json()
    total_lines = 0
    for file in files:
        if file["type"] == "file":
            download_url = file["download_url"]
            file_response = requests.get(download_url, headers=headers)
            lines = file_response.text.split("\n")
            total_lines += len(lines)
    return total_lines

def count_lines_of_code_in_all_repositories(username, token):
    repositories = get_repositories(username, token)
    total_lines = 0
    for repo in repositories:
        lines_in_repo = count_lines_of_code(repo, token)
        total_lines += lines_in_repo
        print(f"Lines in {repo}: {lines_in_repo}")
    print(f"Total lines: {total_lines}")

count_lines_of_code_in_all_repositories("YOUR_USERNAME", "YOUR_TOKEN")
