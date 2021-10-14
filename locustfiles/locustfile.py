from locust import HttpUser, task


class HelloWorld(HttpUser):
    @task
    def single_user(self):
        response = self.client.get("users/2")
        print("Response:", response.content)

    host = "https://reqres.in/api/"
