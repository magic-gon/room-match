import unittest
from main import calculate_embedding_similarity, compute_numeric_similarity, compute_categorical_similarity, compute_levenshtein_similarity
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import pairwise_distances
from Levenshtein import distance as lev_distance
import openai

class TestUnit(unittest.TestCase):
    def test_calculate_embedding_similarity(self):
        description1 = "Room with a beautiful view of the city."
        description2 = "Room with an amazing city view."
        similarity = calculate_embedding_similarity(description1, description2)
        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, -1)
        self.assertLessEqual(similarity, 1)

    def test_compute_numeric_similarity(self):
        room_1 = [1, 2, 3]
        room_2 = [4, 5, 6]
        similarity = compute_numeric_similarity(room_1, room_2)
        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, 0)

    def test_compute_categorical_similarity(self):
        room_1 = {'type': 'single', 'view': 'sea'}
        room_2 = {'type': 'double', 'view': 'sea'}
        categorical_columns = ['type', 'view']
        similarity = compute_categorical_similarity(room_1, room_2, categorical_columns)
        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, 0)
        self.assertLessEqual(similarity, 1)

    def test_compute_levenshtein_similarity(self):
        description_1 = "Room with a beautiful view of the city."
        description_2 = "Room with an amazing city view."
        similarity = compute_levenshtein_similarity(description_1, description_2)
        self.assertIsInstance(similarity, float)
        self.assertGreaterEqual(similarity, 0)
        self.assertLessEqual(similarity, 1)

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "API is running"})

    def test_get_owner(self):
        response = self.app.get('/owner')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"owner": "Gonzalo Hernández"})

if __name__ == '__main__':
    unittest.main()