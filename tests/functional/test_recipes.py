"""Functional tests for model endpoint."""


def test_predict_endpoint_post(test_client):
    """Post request to model endpoint.

    GIVEN a Flask application configured for testing
    WHEN the '/api/predict' endpoint is requested (POST)
    THEN check that the response is valid
    """
    response = test_client.post(
        '/api/predict',
        json={
            "text": """As they rounded a bend in the path that ran beside the
            river, Lara recognized the silhouette of a fig tree atop a nearby 
            hill. The weather was hot and the days were long. The fig tree was 
            in full leaf, but not yet bearing fruit.\nSoon Lara spotted other 
            landmarks—an outcropping of limestone beside the path that had a 
            silhouette like a man’s face, a marshy spot beside the river where 
            the waterfowl were easily startled, a tall tree that looked like a 
            man with his arms upraised. They were drawing near to the place 
            where there was an island in the river."""
        }
    )
    assert response.status_code == 200
    assert "prediction" in response.json


def test_predict_endpoint_with_put(test_client):
    """Put request to model endpoint.

    GIVEN a Flask application configured for testing
    WHEN the '/api/predict' endpoint is requested (PUT)
    THEN check that the response is valid
    """
    response = test_client.put(
        '/api/predict', 
        json={
            "text": """As they rounded a bend in the path that ran beside the
            river, Lara recognized the silhouette of a fig tree atop a nearby 
            hill. The weather was hot and the days were long. The fig tree was 
            in full leaf, but not yet bearing fruit.\nSoon Lara spotted other 
            landmarks—an outcropping of limestone beside the path that had a 
            silhouette like a man’s face, a marshy spot beside the river where 
            the waterfowl were easily startled, a tall tree that looked like a 
            man with his arms upraised. They were drawing near to the place 
            where there was an island in the river."""
        }
    )

    assert response.status_code == 405
