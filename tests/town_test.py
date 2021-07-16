import json
import unittest
from unittest import TestCase
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from tests.mock_objects.town_logic_mock import MockTownLogic
from services.town import TownLogic


app.dependency_overrides[TownLogic] = MockTownLogic


class TestTown(TestCase):

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_get_all(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.get('/api/town/')
            self.assertEqual(r.status_code, 200)

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_get_one_success(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.get('/api/town/1/')
            self.assertEqual(r.status_code, 200)

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_get_one_not_found(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.get('/api/town/10/')
            self.assertEqual(r.status_code, 404)

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_create_success(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.post('/api/town/', data=json.dumps({"name": "name", "altitude": 3, "longitude": 4}))
            self.assertEqual(r.status_code, 201)

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_update_success(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.put('/api/town/1/', data=json.dumps({"name": "name", "altitude": 3, "longitude": 4}))
            self.assertEqual(r.status_code, 201)

    @patch('main.view.town.TownLogic', new_callable=MockTownLogic)
    def test_update_not_found(self, *args, **kwargs):
        with TestClient(app) as client:
            r = client.put('/api/town/10/', data=json.dumps({"name": "name", "altitude": 3, "longitude": 4}))
            self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()
