import re

class ClientInfo():

    def __init__(self, client_address):
        self.client_address = client_address
        self.client_nickname = "user" + re.search(r"\, (.*?)\)", str(client_address)).group(1)

    def change_nickname(self, new_name):
        self.client_nickname = new_name


    def get_nickname(self):
        return self.client_nickname

    def get_address(self):
        return self.client_address