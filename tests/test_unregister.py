def test_unregister_removes_participant(client):
    response = client.delete(
        "/activities/Chess Club/unregister", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 200
    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Not A Real Club/unregister", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 404


def test_unregister_not_signed_up_returns_400(client):
    response = client.delete(
        "/activities/Chess Club/unregister", params={"email": "notsignedup@mergington.edu"}
    )

    assert response.status_code == 400
