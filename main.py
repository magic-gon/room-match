from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/room_match', methods=['POST'])
def room_match():
    try:
        # Parse the incoming JSON request
        payload = request.get_json()
        if not payload:
            return jsonify({"error": "Invalid or missing JSON payload"}), 400
        
        # Validate required fields
        if 'referenceCatalog' not in payload or 'inputCatalog' not in payload:
            return jsonify({"error": "Missing required fields: 'referenceCatalog' and 'inputCatalog'"}), 400
        
        reference_catalog = payload['referenceCatalog']
        input_catalog = payload['inputCatalog']
        
        # Check if referenceCatalog and inputCatalog are non-empty lists
        if not isinstance(reference_catalog, list) or not reference_catalog:
            return jsonify({"error": "'referenceCatalog' must be a non-empty list"}), 400
        
        if not isinstance(input_catalog, list) or not input_catalog:
            return jsonify({"error": "'inputCatalog' must be a non-empty list"}), 400
        
        # Sample hardcoded response for demonstration purposes
        response_data = {
            "Results": [
                {
                    "cleanRoomName": "classic room",
                    "mappedRooms": [
                        {
                            "cleanSupplierRoomName": "classic room accessible r.o.",
                            "roomDescription": "double-person//CLASS//roomOccupancy||classic//CLASS//roomClass||one-double-bed//CLASS//bedType||double-room//CLASS//roomType||+any_view+//CLASS//roomView||accessible//CLASS//roomAccessibility||non-smoking//CLASS//roomSmoking||room-only//CLASS//boardType||non-refundable//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                            "score": 1,
                            "supplierId": "nuitee",
                            "supplierRoomId": "3",
                            "supplierRoomName": "CLASSIC ROOM ADA - ROOM ONLY"
                        }
                    ],
                    "propertyId": "5122906",
                    "propertyName": "Pestana Park Avenue",
                    "roomDescription": "double-person//CLASS//roomOccupancy||classic//CLASS//roomClass||+any_bed+//CLASS//bedType||double-room//CLASS//roomType||+any_view+//CLASS//roomView||non-smoking//CLASS//roomSmoking||+any_food+//CLASS//boardType||+any-refundable+//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                    "roomId": "512290602",
                    "roomName": "Classic Room"
                },
                {
                    "cleanRoomName": "superior room",
                    "mappedRooms": [
                        {
                            "cleanSupplierRoomName": "superior room accessible r.o.",
                            "roomDescription": "double-person//CLASS//roomOccupancy||superior//CLASS//roomClass||one-double-bed//CLASS//bedType||double-room//CLASS//roomType||+any_view+//CLASS//roomView||accessible//CLASS//roomAccessibility||non-smoking//CLASS//roomSmoking||room-only//CLASS//boardType||non-refundable//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                            "score": 1,
                            "supplierId": "nuitee",
                            "supplierRoomId": "5",
                            "supplierRoomName": "SUPERIOR ROOM ADA - ROOM ONLY"
                        }
                    ],
                    "propertyId": "5122906",
                    "propertyName": "Pestana Park Avenue",
                    "roomDescription": "double-person//CLASS//roomOccupancy||superior//CLASS//roomClass||+any_bed+//CLASS//bedType||double-room//CLASS//roomType||+any_view+//CLASS//roomView||non-smoking//CLASS//roomSmoking||+any_food+//CLASS//boardType||+any-refundable+//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                    "roomId": "512290603",
                    "roomName": "Superior Room"
                }
            ],
            "UnmappedRooms": [
                {
                    "cleanSupplierRoomName": "classic room olympic queen bed r.o.",
                    "roomDescription": "double-person//CLASS//roomOccupancy||classic//CLASS//roomClass||one-queen-bed//CLASS//bedType||queen-room//CLASS//roomType||+any_view+//CLASS//roomView||non-smoking//CLASS//roomSmoking||room-only//CLASS//boardType||non-refundable//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                    "supplierId": "nuitee",
                    "supplierRoomId": "2",
                    "supplierRoomName": "Classic Room - Olympic Queen Bed - ROOM ONLY"
                },
                {
                    "cleanSupplierRoomName": "superior room olympic queen bed r.o.",
                    "roomDescription": "double-person//CLASS//roomOccupancy||superior//CLASS//roomClass||one-queen-bed//CLASS//bedType||queen-room//CLASS//roomType||+any_view+//CLASS//roomView||non-smoking//CLASS//roomSmoking||room-only//CLASS//boardType||non-refundable//CLASS//cancellationPolicy||with-windows//CLASS//windows",
                    "supplierId": "nuitee",
                    "supplierRoomId": "10",
                    "supplierRoomName": "Superior Room - Olympic Queen Bed - ROOM ONLY"
                }
            ]
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

@app.route('/owner', methods=['GET'])
def get_owner():
    return jsonify({"owner": "Gonzalo Hernández"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)