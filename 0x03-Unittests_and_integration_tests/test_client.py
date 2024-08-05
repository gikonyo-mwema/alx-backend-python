import unittest
from unittest.mock import patch
from parameterized import parameterized
from your_module import GithubOrgClient  # Replace 'your_module' with the actual module name where GithubOrgClient is defined

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('your_module.get_json', return_value={'login': 'test_org'})
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {'login': 'test_org'})

if __name__ == '__main__':
    unittest.main()

