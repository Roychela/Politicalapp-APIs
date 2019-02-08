import unittest
import json
from tests.V1 import ApiRouteTests

class TestParty(ApiRouteTests):
    def test_get_all_parties(self):
        res = self.client.get("/api/v1/parties")
        result = json.loads(res.data.decode("utf-8"))
        self.assertEqual(result['data'], [])
        self.assertEqual(result["status"], 200)
        self.assertEqual(res.status_code, 200)

    def test_incomplete_format(self):
        res = self.client.post("api/v1/parties", data=json.dumps({
                "id": "35",
                "hqAddress": "Nairobi",
                "name": "ANC"
            }), content_type="application/json")  
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 400)