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
        mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/test/repos'}
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client._public_repos_url,
                         'https://api.github.com/orgs/test/repos')

    @patch('client.GithubOrgClient.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test for GithubOrgClient.public_repos method"""
        expected_repos = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_public_repos_url.return_value = 'https://api.github.com/orgs/test/repos'
        mock_get_json.return_value = expected_repos
        github_client = GithubOrgClient('test')
        repos = github_client.public_repos()
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/test/repos')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for GithubOrgClient.has_license method"""
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.has_license(repo, license_key), expected)

    @patch('client.GithubOrgClient.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos_with_license(self, mock_public_repos_url, mock_get_json):
        """Test for GithubOrgClient.public_repos with license argument"""
        expected_repos = [{'name': 'repo3'}, {'name': 'repo4'}]
        mock_public_repos_url.return_value = 'https://api.github.com/orgs/test/repos'
        mock_get_json.return_value = expected_repos
        github_client = GithubOrgClient('test')
        repos = github_client.public_repos(license="apache-2.0")
        self.assertEqual(repos, expected_repos)
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/test/repos?license=apache-2.0')

if __name__ == "__main__":
    unittest.main()

