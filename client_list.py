
class ClientInfo():

    def __init__(self, client_address, client_nickname = ''):
        self.client_address = client_address
        self.client_nickname = client_nickname

    def nickname(self, new_name):
        self.client_nickname = new_name

    def get_nickname(self):
        return self.client_nickname