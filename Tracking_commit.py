from github import Github
import os
import os.path

# using an access token
github_token = "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"

# Initialize the PyGithub client
g = Github(github_token)

repo_owner = "kdbhai"
repo_name = "CI-CD_pipeline_Project1"

# Get the repository
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Get the latest commit
latest_commit = repo.get_commits().get_page(0)[0]
#print(f"Latest commit in {repo_name}:")
# Print commit details

fname= "commit_log.txt"

if os.path.isfile(fname):
   print("File exist")
else:
     print("File does not exist") 

f = open(fname,'w')
print( latest_commit, file=f)
#print >>f
 
f = open(fname,'r')
file_commit = f.read()
print(f.read())

if latest_commit != file_commit :
    print("This a new commit: ",latest_commit)
