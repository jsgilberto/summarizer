"""Initial configuration for testing."""
import sys
import os
import pytest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, "src"))
from app import app


@pytest.fixture(scope='module')
def test_client():
    """Fixture with flask client.

    Yields:
        Any: the client used to make functional tests
    """
    flask_app = app

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client
