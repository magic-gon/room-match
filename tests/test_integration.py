import unittest
from main import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_room_match(self):
        response = self.app.post('/room_match', json={
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
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Results', response.json)
        self.assertIn('UnmappedRooms', response.json)

if __name__ == '__main__':
    unittest.main()