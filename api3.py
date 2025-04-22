

import requests
import json

url = "https://api.webinarjam.com/everwebinar/registrants"

payload = {
    "api_key": "9deb35c5-a85c-469e-921e-8ec2673d03ac",
    "webinar_id": "10",
    "first_name": "Amit",
    "last_name": "",
    "email": "amit@example.com",
    "phone_country_code": "+91",
    "phone": "9876543210",
    "schedule": "44",
    "timezone": "GMT+05:30"
}

headers = {
    "Content-Type": "application/json"
}

# Send the request
res = requests.post(url, json=payload, headers=headers)

# Print raw response status and body
print("Status Code:", res.status_code)
print("Raw Response Text:", res.text)

# Try to parse and pretty-print the JSON response
try:
    data = res.json()
    print("\n✅ JSON Response:")
    print(json.dumps(data, indent=4))  # Nicely formatted JSON
except requests.exceptions.JSONDecodeError:
    print("\n❌ Response is not in JSON format.")



try:
    data = res.json()

    # Extract specific fields
    name = data.get("registrant", {}).get("first_name", "Name not found")
    email = data.get("registrant", {}).get("email", "Email not found")

    print(f"Name: {name}")
    print(f"Email: {email}")

except requests.exceptions.JSONDecodeError:
    print("❌ Response is not in JSON format.")

