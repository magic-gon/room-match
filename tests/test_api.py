import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_room_match(self):
        url = "http://localhost:5000/room_match"
        payload = {
            "referenceCatalog": [
                {
                    "propertyName": "Pestana Park Avenue",
                    "propertyId": "5122906",
                    "referenceRoomInfo": [
                        {"roomId": "512290602", "roomName": "Classic Room"},
                        {"roomId": "512290603", "roomName": "Superior Room"}
                    ]
                }
            ],
            "inputCatalog": [
                {
                    "cleanSupplierRoomName": "classic room accessible r.o.",
                    "roomDescription": "double-person//CLASS//roomOccupancy||classic//CLASS//roomClass||one-double-bed//CLASS//bedType||double-room//CLASS//roomType||+any_view+//CLASS//roomView||accessible//CLASS//roomAccessibility||non-smoking//CLASS//roomSmoking||room-only//CLASS//boardType||non-refundable//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                    "supplierId": "nuitee",
                    "supplierRoomId": "3",
                    "supplierRoomName": "CLASSIC ROOM ADA - ROOM ONLY"
                }
            ]
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Results', response.json())
        self.assertIn('UnmappedRooms', response.json())

    def test_health_check(self):
        url = "http://localhost:5000/health"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "API is running"})

    def test_get_owner(self):
        url = "http://localhost:5000/owner"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"owner": "Gonzalo Hernández"})

if __name__ == '__main__':
    unittest.main()