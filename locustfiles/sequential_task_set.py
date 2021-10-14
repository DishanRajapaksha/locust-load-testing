import json
import logging

from locust import task, tag, SequentialTaskSet, HttpUser

# SequentialTaskSet is a TaskSet whose tasks will be executed in the order that they are declared.
# https://docs.locust.io/en/latest/tasksets.html#sequentialtaskset-class
from models.user_create_response import UserCreateResponse


class UserCRUDSequentialTaskSet(SequentialTaskSet):
    created_user: UserCreateResponse

    @tag('admin')
    @task
    def create(self):
        print("========== POST ==========")
        response = self.client.post("users", json={
            "name": "morpheus",
            "job": "leader"
        })
        body = json.loads(response.content)
        self.created_user = UserCreateResponse(**body)
        print("Response:", response.content)
        print("======== POST END =========")

    @tag('admin')
    @task
    def read(self):
        logging.info("========== GET ==========")
        response = self.client.get(f"users/{self.created_user.id}")
        logging.info("Response:", response.content)
        logging.info("======== GET END =========")

    @tag('admin')
    @task
    def update(self):
        logging.debug("========== PUT ===========")
        response = self.client.put(f"users/{self.created_user.id}", json={
            "name": "morpheus",
            "job": "zion resident"
        })
        logging.info("Response:", response.content)
        logging.debug("======== PUT END =========")

    @tag('admin')
    @task
    def delete(self):
        print("========== DELETE ===========")
        response = self.client.delete(f"users/{self.created_user.id}")
        print("Response:", response.content)
        print("======== DELETE END =========")

    @task
    def stop(self):
        self.user.environment.reached_end = True
        self.user.environment.runner.quit()


class LoadTestHttpUser(HttpUser):
    host = "https://reqres.in/api/"
    tasks = [UserCRUDSequentialTaskSet]
