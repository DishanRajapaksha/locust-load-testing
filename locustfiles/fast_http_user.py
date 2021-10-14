from locust import FastHttpUser, task

from locustfiles.user_list_task_set import UserListTaskSet


class WebsiteUser(FastHttpUser):

    host = "http://127.0.0.1:8089"
    # some things you can configure on FastHttpUser
    # connection_timeout = 60.0
    # insecure = True
    # max_redirects = 5
    # max_retries = 1
    # network_timeout = 60.0

    tasks = [UserListTaskSet]
