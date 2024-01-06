import requests
from dotenv import load_dotenv
import os
load_dotenv()
def register_customer(data):
    shopurl=os.environ.get("SHOP_URL")
    customer_endpoint = f'{shopurl}/admin/api/2023-10/customers.json'
    access_token = os.environ.get("API_KEY") 
    # Customer data
    customer_data = data
    # Headers with access token
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token
    }
    # Make the POST request to create the customer
    response = requests.post(customer_endpoint, json=customer_data, headers=headers)

    # Check the response
    if response.status_code == 201:
        return "Customer successfully created:", response.json()['customer']
    elif response.status_code == 422:
      raise ValueError(f"Failed to create customer. Status code:, {response.status_code},Response: {response.text}")
    else:
        raise ValueError(f"Unknown error occurred during customer registration. Status code: {response.status_code}. Response: {response.text}")