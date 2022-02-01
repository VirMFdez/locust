
from locust import HttpUser,User,task,between

class MyUser(HttpUser):

    wait_time = between(1,2)
    host = "http://newtours.demoaut.com"

    @task
    def login_URL(self):
        print("Im loggin into URL")