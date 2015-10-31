from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that login behaves correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True)
        self.assertTrue(b'You were just logged in' in response.data)

    # Ensure that login behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
            data=dict(username='', password=''),
            follow_redirects=True)
        self.assertTrue(b'Invalid credentials' in response.data)

    # Ensure that the logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post('/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)

    # Ensure that the main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to log in first.' in response.data)


if __name__ == '__main__':
    unittest.main()
