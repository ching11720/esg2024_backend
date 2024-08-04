# tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee

class EmployeeViewTest(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
                EID='022024080005',
                name='test5',
                gender=1,
                phone='0912345678',
                email='a@a.com',
                nation='TW',
                status=1)

    def test_delete_employee(self):
        response = self.client.delete('/admins/employee/delete', {'EID': '022024080005', 'name': 'test5'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.status, 0)
