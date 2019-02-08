import unittest
import json
from tests.V1 import ApiRouteTests

class TestOffice(ApiRouteTests):
    def test_get_all_offices(self):
        res = self.client.get("/api/v1/offices")
        result = json.loads(res.data.decode("utf-8"))
        self.assertEqual(result['data'], [])
        self.assertEqual(result["status"], 200)
        self.assertEqual(res.status_code, 200)

    def test_incomplete_format(self):
        res = self.client.post("api/v1/offices", data=json.dumps({
                "id": "35",
                "type": "Legislature"
            }), content_type="application/json")  
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 400)
    

