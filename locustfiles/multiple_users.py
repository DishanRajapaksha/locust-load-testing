import logging
import random

from locust import TaskSet, HttpUser, task

Credentials = [("Dishan1", "MTIzNDU="),
               ("Dishan2", "MTIzNDU="),
               ("Dishan3", "MTIzNDU="),
               ("Dishan4", "MTIzNDU="),
               ("Dishan5", "MTIzNDU=")]


class UserBehaviour(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.username = None
        self.password = None
        self.token = None
        self.laptopId = random.randint(1, 12)

    def on_start(self):
        self.username, self.password = Credentials.pop()
        with self.client.post("/login", json={"username": self.username, "password": self.password},
                              catch_response=True) as response:
            try:
                response = response.json()
                logging.info("Login response", response)
                token = response.split(":")[1]
                logging.info("Login token", response)
                self.client.headers.update({'authorization': token})
            except Exception as error:
                logging.error("Authentication failed", error)

    @task(1)
    def selectALaptop(self):
        logging.info("Selecting a laptop", self.laptopId)
        response = self.client.post("/view", json={"id": self.laptopId})
        logging.info("Laptop selected", response)

    @task(1)
    def addToCart(self):
        logging.info("Adding to cart ", self.laptopId)
        response = self.client.post("/addtocart", json={"prod_id": self.laptopId})
        logging.info("Added to cart", response)

    @task(1)
    def viewCart(self):
        logging.info("Viewing cart ", self.laptopId)
        response = self.client.post("/viewcart")
        logging.info("Cart", response, response)


class User(HttpUser):
    tasks = {UserBehaviour}
    min_wait = 5000
    max_wait = 15000

    host = "https://api.demoblaze.com"
