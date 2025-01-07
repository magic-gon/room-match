import requests
import json

# URL de la API y clave de autenticación
url = "http://localhost:5000/room_match"

# Datos de entrada (payload)
payload = {
    "debug": True,
    "run_ner": True,
    "referenceCatalog": [
        {
            "propertyName": "Pestana Park Avenue",
            "propertyId": "5122906",
            "referenceRoomInfo": [
                {"roomId": "512290602", "roomName": "Classic Room"},
                {"roomId": "512290603", "roomName": "Superior Room"},
                {"roomId": "512290604", "roomName": "Superior Room with City View"},
                {"roomId": "512290605", "roomName": "Balcony Room"},
                {"roomId": "512290608", "roomName": "Classic Room - Disability Access"},
                {"roomId": "512290609", "roomName": "Superior Room - Disability Access"},
                {"roomId": "512290610", "roomName": "Junior Suite - Disability Access"}
            ]
        }
    ],
    "inputCatalog": [
        {
            "supplierId": "nuitee",
            "supplierRoomInfo": [
                {"supplierRoomId": "2", "supplierRoomName": "Classic Room - Olympic Queen Bed - ROOM ONLY"},
                {"supplierRoomId": "3", "supplierRoomName": "CLASSIC ROOM ADA - ROOM ONLY"},
                {"supplierRoomId": "5", "supplierRoomName": "SUPERIOR ROOM ADA - ROOM ONLY"},
                {"supplierRoomId": "10", "supplierRoomName": "Superior Room - Olympic Queen Bed - ROOM ONLY"},
                {"supplierRoomId": "6", "supplierRoomName": "Superior City View - Olympic Queen Bed - ROOM ONLY"},
                {"supplierRoomId": "7", "supplierRoomName": "Balcony Room - Olympic Queen Bed - ROOM ONLY"}
            ]
        }
    ]
}

# Encabezados del request
headers = {
    "Content-Type": "application/json"
}

try:
    # Enviar el request POST a la API
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    elif response.status_code == 400:
        print("Bad Request:", response.json().get("error", "Unknown error"))
    elif response.status_code == 500:
        print("Server Error:", response.json().get("error", "Unknown error"))
    else:
        print(f"Unexpected Status Code: {response.status_code}")
        print("Response:", response.text)

except requests.exceptions.Timeout:
    print("Error: The request timed out. Please try again later.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API. Please check the server URL.")

except requests.exceptions.RequestException as e:
    print(f"Error: An unexpected error occurred - {str(e)}")
