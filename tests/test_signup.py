def test_signup_adds_participant(client):
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"}
    )

    assert response.status_code == 200
    activities = client.get("/activities").json()
    assert "newstudent@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Not A Real Club/signup", params={"email": "someone@mergington.edu"}
    )

    assert response.status_code == 404


def test_signup_duplicate_email_returns_400(client):
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 400
