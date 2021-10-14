from locust import HttpUser, TaskSet

from common.authentication import login
from locustfiles.user_list_task_set import UserListTaskSet


class OnStartEndEvents(TaskSet):

    # Called when a User starts executing this TaskSet
    # https://docs.locust.io/en/latest/writing-a-locustfile.html#on-start-and-on-stop-methods
    def on_start(self):
        login(self)

    # Called when a User stops executing this TaskSet.
    # E.g. when TaskSet.interrupt() is called or when the User is killed
    def on_stop(self):
        print("Stopping")

    tasks = [UserListTaskSet]


# A user class represents one user.
# Locust will spawn one instance of the User class for each user that is being simulated.
# https://docs.locust.io/en/latest/writing-a-locustfile.html
class OnStartEnd(HttpUser):
    host = "https://reqres.in/api/"

    tasks = [OnStartEndEvents]
