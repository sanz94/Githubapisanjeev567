import unittest
import json
import urllib
import requests


def parse_git(user_id, optional_param= "repoCommits"):
    repo_list = []
    try:
        with urllib.request.urlopen("https://api.github.com/users/"+user_id+"/repos") as reporesponse:
            repohtml = reporesponse.read()
            repoans = json.loads(repohtml)
    except urllib.error.HTTPError:
        return "Invalid URL".format("https://api.github.com/users/"+user_id+"/repos")

    print("User {} has {} repositories".format(user_id, str(len(repoans))))

    for repo in repoans:
        repo_list.append(repo["name"])
        try:
            # print("https://api.github.com/repos/" + user_id + repo["name"] + "/commits")
            with urllib.request.urlopen("https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits") as commitresponse:
                commithtml = commitresponse.read()
                commitans = json.loads(commithtml)
        except urllib.error.HTTPError:
            return "Invalid URL".format("https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits")

        print("Repo: {} Number of commits: {}".format(repo["name"], len(commitans)))
    if optional_param == "repocount":
        return len(repoans)
    elif optional_param == "repoCommits":

        return repo_list


class TestCases(unittest.TestCase):

    def testInvalid(self):
        self.assertEqual(parse_git("invalidinvalidinvalid", "repoCount"), 'Invalid URL')
        self.assertEqual(parse_git("invalidinvalidinvalid", "repoCommits"), 'Invalid URL')

    def testRepoCount(self):

        self.assertEqual(parse_git("sanz94", "repocount"), 15)

    def testRepoList(self):

        self.assertEqual(parse_git("sanz94", "repoCommits"), ['CPE593_2017F', 'Daizo-AI-chatbot',
                                                              'Githubapisanjeev567', 'Kriya-website',
                                                              'QtClientServerCPP', 'Rain-Data', 'RLAI',
                                                              'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database',
                                                              'TrackPro-Tracking-app', 'Triangle567',
                                                              'University-Repository', 'Wall-E'])


if __name__ == '__main__':
    unittest.main()
print(parse_git("sanz94"))
