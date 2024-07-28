import subprocess

cmd = ["pip install PyGithub"]

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    return stdout, stderr, return_code

stdout, stderr, return_code = run_command(cmd[-1])

from github import Github

# Authentication is defined via github.Auth
from github import Auth

with open(hidden, "r") as f:
    access_token = f.read().strip()

# using an access token
auth = Auth.Token(access_token)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()
