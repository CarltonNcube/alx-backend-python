#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test for GithubOrgClient.org method"""
        expected = {'org': org_name}
        mock_get_json.return_value = expected
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org, expected)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test for GithubOrgClient._public_repos_url property"""
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/test/repos'
        }
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client._public_repos_url,
                         'https://api.github.com/orgs/test/repos')

    @patch('client.GithubOrgClient.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test for GithubOrgClient.public_repos method"""
        expected_repos = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_public_repos_url.return_value = \
            'https://api.github.com/orgs/test/repos'
        mock_get_json.return_value = expected_repos
        github_client = GithubOrgClient('test')
        repos = github_client.public_repos()
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/test/repos'
        )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for GithubOrgClient.has_license method"""
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.has_license(repo, license_key), expected)


class TestGithubOrgClientIntegration(unittest.TestCase):
    """Integration tests for the `GithubOrgClient` class."""
    
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': TEST_PAYLOAD[0][0],
            'https://api.github.com/orgs/google/repos': TEST_PAYLOAD[0][1],
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            TEST_PAYLOAD[0][2],
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            TEST_PAYLOAD[0][3],
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
