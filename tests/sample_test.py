from validators.json_schema import json_matches_schema


def test_something():
    assert json_matches_schema({"name": "Eggs", "price": 34.99}, "sample.json")
    assert json_matches_schema({"name": "Eggs", "price": "Invalid"}, "sample.json")
