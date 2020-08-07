import random

from locust import HttpUser, task, between
import secret_config

class HttpUsers(HttpUser):
    wait_time = between(0.01,0.02)
    @task(10)
    def get_ifr(self):
        region_id = random.randint(1,100)
        self.client.get(f'/get_version?region_id={region_id}')

    @task(5)
    def get_fbc(self):
        region_id = random.randint(100,200)
        self.client.get(f'/get_version?region_id={region_id}')

    def get_nothing(self):
        self.client.get('/')
    
    host = secret_config.host
