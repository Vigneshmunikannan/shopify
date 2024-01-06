import unittest
from unittest.mock import MagicMock, patch
from src.update import update_customer  # Replace with the actual module name

class TestUpdateCustomer(unittest.TestCase):
    @patch('src.update.requests.put')
    def test_update_customer_success(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'customer': {'id': 123, 'first_name': 'Deepan'}}
        mock_put.return_value = mock_response
        customer_id = 123
        update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
        result = update_customer(customer_id, update_data)
        expected_result = ("Customer successfully updated:", {'id': 123, 'first_name': 'Deepan'})
        self.assertEqual(result, expected_result)
    
    @patch('src.update.requests.put')
    def test_update_customer_notfound(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = {'errors: Not Found'}
        mock_put.return_value = mock_response
        customer_id = 12345
        update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
        with self.assertRaises(ValueError) as context:
                update_customer(customer_id,update_data)
        self.assertEqual(str(context.exception),("Error: Customer not found. Status code: 404. Response: {'errors: Not Found'}"))

    
    @patch('src.register.requests.put')
    def test_update_customer_phone_already_exits(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"phone":["Phone has already been taken"]}'
        mock_put.return_value = mock_response
        customer_id = 123456
        update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
        with self.assertRaises(ValueError) as context:
            update_customer(customer_id,update_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"phone":["Phone has already been taken"]}'))

    @patch('src.register.requests.put')
    def test_update_customer_email_already_exits(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"Email":["Email has already been taken"]}'
        mock_put.return_value = mock_response
        customer_id = 123456
        update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
        with self.assertRaises(ValueError) as context:
            update_customer(customer_id,update_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"Email":["Email has already been taken"]}'))


    @patch('src.register.requests.put')
    def test_update_customer_emailandphone_already_exits(self, mock_put):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"phone":["Phone has already been taken"]},{"Email":["Email has already been taken"]}'
        mock_put.return_value = mock_response
        customer_id = 123456
        update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
        with self.assertRaises(ValueError) as context:
            update_customer(customer_id,update_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"phone":["Phone has already been taken"]},{"Email":["Email has already been taken"]}'))

    @patch('src.register.requests.put')
    def test_register_customer_unknown_errors(self, mock_put):
            mock_response = MagicMock()
            mock_response.status_code = 500
            mock_response.text = 'Internal Server Error'
            mock_put.return_value = mock_response
            customer_id = 123456
            update_data = {'first_name': 'Vignesh', 'last_name': 'M'}
            with self.assertRaises(ValueError) as context:
                update_customer(customer_id,update_data)
            self.assertEqual(str(context.exception),('Unknown error occurred during customer update. Status code: 500. Response: Internal Server Error'))




