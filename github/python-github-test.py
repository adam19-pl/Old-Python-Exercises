import unittest
import python_repos_refactor as prr

class PythonReposRefactorTestCase(unittest.TestCase):

    def setUp(self):
        self.r = prr.get_response()
        self.repo_dicts = prr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = prr.get_repo_infos(self.repo_dict)

    def test_get_response(self):
        """Test that we get a valid response."""
        self.assertEqual(self.r.status_code, 200)



if __name__ == '__main__':
    unittest.main()