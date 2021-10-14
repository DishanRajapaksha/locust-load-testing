from locust import HttpUser, constant
from locust import LoadTestShape
from locustfiles.user_list_task_set import UserListTaskSet


class StagesLoadTestShape(LoadTestShape):
    stages = [
        {"duration": 15, "users": 10, "spawn_rate": 10},
        {"duration": 45, "users": 50, "spawn_rate": 10},
        {"duration": 75, "users": 100, "spawn_rate": 10},
        {"duration": 90, "users": 30, "spawn_rate": 10},
        {"duration": 105, "users": 10, "spawn_rate": 10},
        {"duration": 120, "users": 1, "spawn_rate": 1}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None


class WebsiteUser(HttpUser):
    host = "https://reqres.in/api/"
    wait_time = constant(0.5)
    tasks = [UserListTaskSet]
