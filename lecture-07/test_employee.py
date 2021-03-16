import unittest
from unittest.mock import patch
from employee import employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey','Schafer',50000)
        self.emp_2 = Employee('Sau','Smith',60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        # emp_1 = Employee('Corey','Schafer',50000)
        # emp_2 = Employee('Sau','Smith',60000)

        self.assertEqual(emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email, 'Sau.Smith@email.com')

        self.emp_1.first ="John"
        self.emp_2.first='Jane'

        self.assertEqual(emp_1.email,'John.Schafer@email.com')
        self.assertEqual(emp_2.email,'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        # emp_1 = Employee('Corey','Schafer',50000)
        # emp_2 = Employee('Sau','Smith',60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sau Smith')

        self.emp_1.first ="John"
        self.emp_2.first='Jane'

        self.assertEqual(emp_1.fullname,'John Schafer')
        self.assertEqual(emp_2.fullname,'Jane Smith')
    
    def test_apply_raise(self):
        print('test_app;y_raise')
        # emp_1 = Employee('Corey','Schafer',50000)
        # emp_2 = Employee('Sau','Smith',60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(emp_1.pay,52500)
        self.assertEqual(emp_2.pay,63000)

    def test_monthly_schedule(self):
        with patch ('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text ='Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()