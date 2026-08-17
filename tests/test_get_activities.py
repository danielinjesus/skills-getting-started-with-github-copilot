def test_get_activities_returns_known_activity(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data


def test_activity_has_expected_fields(client):
    response = client.get("/activities")

    chess_club = response.json()["Chess Club"]
    assert set(["description", "schedule", "max_participants", "participants"]) <= set(chess_club.keys())
    assert isinstance(chess_club["participants"], list)
