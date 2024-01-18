import json
import os
import pytest

from src.data_base import Database
from src.search_engine import SearchEngine
from tools.path_tool import get_project_root


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def search_engine():
    return SearchEngine()


@pytest.fixture
def search_term():
    return "banana"


@pytest.fixture
def invalid_search_term():
    return "tomato"


@pytest.fixture
def data_test():
    # Construct the path to the test data JSON file
    data_file_path = os.path.join(get_project_root(), 'data', 'test_data.json')
    # Load test data from a JSON file
    with open(data_file_path) as f:
        test_data = json.load(f)
    return test_data
