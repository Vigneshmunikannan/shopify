import requests
from dotenv import load_dotenv
import os

load_dotenv()

def update_customer(customer_id,updatedata):
    shopurl=os.environ.get("SHOP_URL")
    customer_endpoint = f'{shopurl}/admin/api/2023-10/customers/{customer_id}.json'
    access_token = os.environ.get("API_KEY")     
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Shopify-Access-Token": access_token
}

    response=requests.put(customer_endpoint,json={"customer": updatedata},headers=headers)

    if response.status_code == 200:
        return "Customer successfully updated:", response.json()['customer']
    elif response.status_code == 404:
        raise ValueError(f"Error: Customer not found. Status code: {response.status_code}. Response: {response.text}")
    elif response.status_code == 422:
      raise ValueError(f"Failed to create customer. Status code:, {response.status_code},Response: {response.text}")
    else:
        raise ValueError(f"Unknown error occurred during customer update. Status code: {response.status_code}. Response: {response.text}")

    
    