from .repo import Repo

class TestRepoCase(): 
    def test_name(self, repo_test_data):
        repo = Repo(repo_test_data)
        assert repo._name == "Test Repo Name"