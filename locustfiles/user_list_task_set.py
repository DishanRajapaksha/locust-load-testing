from locust import TaskSet, tag, task


# Collection of tasks
# https://docs.locust.io/en/latest/tasksets.html#taskset-class
class UserListTaskSet(TaskSet):

    @tag('list')
    @task
    def single_user(self):
        response = self.client.get("users/2")
        print("Response:", response.content)
