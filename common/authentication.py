import logging
from json import JSONDecodeError

from common.users import users


def login(self):
    logging.info("Sending login request")
    with self.client.post("login",
                          json=users[0], catch_response=True) as response:
        try:
            json_response = response.json()
            logging.info("Login response", json_response)
            if json_response["token"] is None:
                logging.error("Invalid Login")
            logging.info("Successful login", json_response["token"])
            self.client.headers.update({'authorization': json_response["token"]})
        except JSONDecodeError:
            logging.error("Response could not be decoded as JSON")
        except KeyError:
            logging.error("Response did not contain expected keys")