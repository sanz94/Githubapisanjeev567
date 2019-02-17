import requests
import json
import urllib

def parseGit(user_id):
    repo_list = []
    try:
        with urllib.request.urlopen("https://api.github.com/users/"+user_id+"/repos") as reporesponse:
            repohtml = reporesponse.read()
            repoans = json.loads(repohtml)
    except:
        return "Invalid URL".format("https://api.github.com/users/"+user_id+"/repos")

    print("User {} has {} repositories".format(user_id, str(len(repoans))))

    for repo in repoans:
        repo_list.append(repo["name"])
        try:
            # print("https://api.github.com/repos/" + user_id + repo["name"] + "/commits")
            with urllib.request.urlopen("https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits") as commitresponse:
                commithtml = commitresponse.read()
                commitans = json.loads(commithtml)
        except:
            return "Invalid URL {}".format("https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits")

        print("Repo: {} Number of commits: {}".format(repo["name"], len(commitans)))
    return repo_list


print(parseGit("sanz94"))
