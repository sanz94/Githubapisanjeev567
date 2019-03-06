import unittest
import json
import requests
from unittest import mock



def parse_git(user_id, optional_param= "repoCommits"):
    repo_list = []

    try:
        reporesponse = requests.get("https://api.github.com/users/"+user_id+"/repos")
        repo_json = reporesponse.text
        if optional_param == "repoJson":
            return repo_json
        repos = json.loads(repo_json)
        result = []

        for item in repos:
            result.append(item['name'])

        return "Invalid URL".format("https://api.github.com/users/"+user_id+"/repos")

    except Exception as e:

        return e

    print("User {} has {} repositories".format(user_id, str(len(result))))

    for rep in result:
        repo_list.append(rep["name"])
        try:
            reporesponse = requests.get("https://api.github.com/repos/" + user_id + "/" + rep["name"] + "/commits")
            repo_json = reporesponse.text
            repos = json.loads(repo_json)
            result = []

            for item in repos:
                result.append(item['name'])
        except Exception as e:
            return e

    if optional_param == "repocount":
        return len(result)
    elif optional_param == "repoCommits":
        return repo_list


class MockResponse:

    def __init__(self, json):
        self.text = json


class TestCases(unittest.TestCase):

    @mock.patch('requests.get')
    def testMock(self, mockedReq):

        mockedReq.return_value = MockResponse('[{"name": "CPE593_2017F"}, {"name": "Daizo-AI-chatbot"}, {"name": "Githubapisanjeev567"}, {"name": "Kriya-website"}, {"name": "QtClientServerCPP"}, {"name": "Rain-Data"}, {"name": "RLAI"}, {"name": "Smart-Home"}, {"name": "SSW-555"}, {"name": "SSW567"}, {"name": "Student-Database"}, {"name": "TrackPro-Tracking-app"}, {"name": "Triangle567"}, {"name": "University-Repository"}, {"name": "Wall-E"}]')
        self.assertEqual(parse_git('sanz94', 'repoJson'), mockedReq.return_value.text)
        self.assertEqual(parse_git('sanz94', 'repoCount'), 15)


if __name__ == '__main__':
    unittest.main()

