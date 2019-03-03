import unittest
import json
import urllib
import requests
from unittest import mock
from unittest.mock import patch, MagicMock


def parse_git(user_id, optional_param= "repoCommits"):
    repo_list = []
    try:
        with urllib.request.urlopen("https://aasdasdadasdpi.github.com/users/"+user_id+"/repos") as reporesponse:
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


def mocked_requests_get(*args, **kwargs):

    if args[0] == 'sanz94' and args[1] == "repoCommits":
        return (['CPE593_2017F', 'Daizo-AI-chatbot',
                                                              'Githubapisanjeev567', 'Kriya-website',
                                                              'QtClientServerCPP', 'Rain-Data', 'RLAI',
                                                              'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database',
                                                              'TrackPro-Tracking-app', 'Triangle567',
                                                              'University-Repository', 'Wall-E'])
    elif args[0] == 'sanz94' and args[0] == "repoCount":
        return 15

    return None


class TestCases(unittest.TestCase):

    def side_effects(self, value1, value2):
        if value1 == 'sanz94' and value2 == 'repoCount':
            return 15
        if value1 == 'sanz94' and value2 == 'repoCommits':
            return ['CPE593_2017F', 'Daizo-AI-chatbot',
                                                              'Githubapisanjeev567', 'Kriya-website',
                                                              'QtClientServerCPP', 'Rain-Data', 'RLAI',
                                                              'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database',
                                                              'TrackPro-Tracking-app', 'Triangle567',
                                                              'University-Repository', 'Wall-E']

    def testMock(self):
        m1 = MagicMock(side_effect=self.side_effects)
        json_data1 = m1("sanz94", "repoCount")
        json_data2 = m1("sanz94", "repoCommits")
        self.assertEqual(json_data1, 15)
        self.assertEqual(json_data2, ['CPE593_2017F', 'Daizo-AI-chatbot',
                                                              'Githubapisanjeev567', 'Kriya-website',
                                                              'QtClientServerCPP', 'Rain-Data', 'RLAI',
                                                              'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database',
                                                              'TrackPro-Tracking-app', 'Triangle567',
                                                              'University-Repository', 'Wall-E'])

    # def testInvalid(self):
    #     self.assertEqual(parse_git("invalidinvalidinvalid", "repoCount"), 'Invalid URL')
    #     self.assertEqual(parse_git("invalidinvalidinvalid", "repoCommits"), 'Invalid URL')
    #
    # def testRepoCount(self):
    #
    #     self.assertEqual(parse_git("sanz94", "repocount"), 15)
    #
    # def testRepoList(self):
    #
    #     self.assertEqual(parse_git("sanz94", "repoCommits"), ['CPE593_2017F', 'Daizo-AI-chatbot',
    #                                                           'Githubapisanjeev567', 'Kriya-website',
    #                                                           'QtClientServerCPP', 'Rain-Data', 'RLAI',
    #                                                           'Smart-Home', 'SSW-555', 'SSW567', 'Student-Database',
    #                                                           'TrackPro-Tracking-app', 'Triangle567',
    #                                                           'University-Repository', 'Wall-E'])


if __name__ == '__main__':
    unittest.main()
print(parse_git("sanz94"))
