import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

# Snapshot the original in-memory data so each test starts from a known state
_ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app_module.app)
