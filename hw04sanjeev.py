import requests
import unittest
import json
import urllib

def parseGit(user_id, optional_param= "repoCommits"):
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
    if optional_param == "repocount":
        return len(repoans)
    elif optional_param == "repoCommits":

        return repo_list

class TestCases(unittest.TestCase):

    def testRepoCount(self):

        self.assertEqual(parseGit("sanz94", "repocount"), 15)

    def testRepoList(self):

        self.assertEqual(parseGit("sanz94", "repoCommits"), ['CPE593_2017F', 'Daizo-AI-chatbot', 'Githubapisanjeev567', 'Kriya-website', 'QtClientServerCPP', 'RLAI', 'Rain-Data', 'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database', 'TrackPro-Tracking-app', 'Triangle567', 'University-Repository', 'Wall-E'])


if __name__ == '__main__':
    unittest.main()
print(parseGit("sanz94"))
