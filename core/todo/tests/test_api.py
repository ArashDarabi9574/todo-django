from datetime import datetime
from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from accounts.models import User

@pytest.fixture
def my_user():
     user = User.objects.create_user(email='user2@example.com', password='password12345',is_verified=True)
     return user

@pytest.mark.django_db
class TestTaskApi:
     client = APIClient()

     def test_get_task_response_200_status(self):

          url = reverse("todo:api:task_list-list")
          
          response = self.client.get(url)
          assert response.status_code == 200

     def test_create_task_response_401_status(self,my_user):
          
          url = reverse("todo:api:task_list-list")
          data = {
               'title' : "pytest",
               'created_date' : datetime.now(),


          }
          response = self.client.post(url,data)
          assert response.status_code == 401

     def test_create_task_response_201_status(self,my_user):
          
          url = reverse("todo:api:task_list-list")
          data = {
               'title' : "pytest",
               'created_date' : datetime.now(),


          }
          self.client.force_authenticate(user=my_user)
          response = self.client.post(url,data)
          assert response.status_code == 201

     # def test_create_task_invalid_response_400_status(self,my_user):
          
     #      url = reverse("todo:api:task_list-list")
     #      data = {
               
     #           'created_date': datetime.now(),
     #      }
     #      self.client.force_authenticate(user=my_user)
     #      response = self.client.post(url,data)
     #      assert response.status_code == 400