import unittest
from unittest.mock import MagicMock, patch
from src.register import register_customer
class TestRegisterCustomer(unittest.TestCase):

    @patch('src.register.requests.post')
    def test_register_customer_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {'customer': {'id': 123, 'first_name': 'Vignesh1','phone':'63749076711','email':'vignesh1@gmail.com','password':'123'}}
        mock_post.return_value = mock_response
        customer_data ={'id': 123, 'first_name': 'Vignesh1','phone':'6374907671','email':'vignesh@gmail.com','password':'123'}
        result = register_customer(customer_data)
        # print(result)
        self.assertEqual(result,("Customer successfully created:",{'id': 123, 'first_name': 'Vignesh1','phone':'63749076711','email':'vignesh1@gmail.com','password':'123'}))

    @patch('src.register.requests.post')
    def test_register_customer_phone(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"phone":["Phone has already been taken"]}'
        mock_post.return_value = mock_response
        customer_data ={'id': 123, 'first_name': 'Vignesh1','phone':'6374907671','email':'vignesh@gmail.com','password':'123'}
        with self.assertRaises(ValueError) as context:
            register_customer(customer_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"phone":["Phone has already been taken"]}'))

    @patch('src.register.requests.post')
    def test_register_customer_email(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"email":["Email has already been taken"]}'
        mock_post.return_value = mock_response
        customer_data ={'id': 123, 'first_name': 'Vignesh1','phone':'6374907671','email':'vignesh@gmail.com','password':'123'}
        with self.assertRaises(ValueError) as context:
            register_customer(customer_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"email":["Email has already been taken"]}'))


    @patch('src.register.requests.post')
    def test_register_customer_emailandphone(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.text = '{"phone":["Phone has already been taken"]},{"email":["Email has already been taken"]}'
        mock_post.return_value = mock_response
        customer_data ={'id': 123, 'first_name': 'Vignesh1','phone':'6374907671','email':'vignesh@gmail.com','password':'123'}
        with self.assertRaises(ValueError) as context:
            register_customer(customer_data)
        self.assertEqual(str(context.exception),('Failed to create customer. Status code:, 422,Response: {"phone":["Phone has already been taken"]},{"email":["Email has already been taken"]}'))


    @patch('src.register.requests.post')
    def test_register_customer_unknown_errors(self, mock_post):
            mock_response = MagicMock()
            mock_response.status_code = 500
            mock_response.text = 'Internal Server Error'
            mock_post.return_value = mock_response
            customer_data ={'id': 123, 'first_name': 'Vignesh1','phone':'6374907671','email':'vignesh@gmail.com','password':'123'}
            with self.assertRaises(ValueError) as context:
                register_customer(customer_data)
            self.assertEqual(str(context.exception),('Unknown error occurred during customer registration. Status code: 500. Response: Internal Server Error'))















    

