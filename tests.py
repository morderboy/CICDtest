import unittest
from fastapi.testclient import TestClient
from main import app


class FastApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_read_hello(self):
        response = self.client.get("/hello/User")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello User"})


if __name__ == '__main__':
    #Run Tests
    unittest.main()
