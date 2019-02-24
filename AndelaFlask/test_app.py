import unittest
import os
import json
from app import create_app, db


class AndelansTestCase(unittest.TestCase):
    """This class represents the andelans test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.andelan = {'name': 'Emmanuel Kiprono','language':'python'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_andelans_creation(self):
        """Test API can create a andelans (POST request)"""
        res = self.client().post('/andelans/', data=self.andelan)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Emmanuel Kiprono', str(res.data))

    def test_api_can_get_all_andelanss(self):
        """Test API can get a andelan (GET request)."""
        res = self.client().post('/andelans/', data=self.andelan)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/andelans/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Emmanuel', str(res.data))

    def test_api_can_get_andelan_by_id(self):
        """Test API can get a single andelan by using it's id."""
        rv = self.client().post('/andelans/', data=self.andelan)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/andelans/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Emmanuel', str(result.data))

    def test_andelan_can_be_edited(self):
        """Test API can edit an existing andelan. (PUT request)"""
        rv = self.client().post(
            '/andelans/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/andelans/1',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/andelans/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_andelan_deletion(self):
        """Test API can delete an existing andelan. (DELETE request)."""
        rv = self.client().post(
            '/andelans/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/andelans/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/andelans/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main(verbosity=2)