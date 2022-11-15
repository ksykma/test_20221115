from django.urls import reverse
from rest_framework.test import APITestCase
# Create your tests here.
class UserSignupTest(APITestCase):
    def signup_test(self):
        url = reverse("users:user_view")
        user_data = {
            "username":"test123",
            "password":"test",
            "email":"test@naver.com",
            "fullname":"test12345"
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual(response.data, {"message":"가입 완료!!"})
