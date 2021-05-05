import pytest

@pytest.fixture
def repo_test_data():
    return {
        "name": "Test Repo Name",
        "description": "description for test repo",
        "language": "test"
    }


@pytest.fixture()
def repo_test_list():
    return [
        { 
            "name": "Test Repo Name",
            "description": "description for test repo",
            "language": "test"
        },
        { 
            "name": "Test Repo Name 2",
            "description": "description for test repo 2",
            "language": "test2"
        }
    ]
    