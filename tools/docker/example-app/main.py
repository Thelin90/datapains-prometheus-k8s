import random
import time
from prometheus_client import start_http_server, Gauge

random_number_metric = Gauge('random_integer', 'Random number generated every 15 sec')

def generate_random_number():
    return random.randint(1, 100000000)

if __name__ == '__main__':
    start_http_server(8000)
    print("Start Prometheus Server 8000")
    
    while True:
        random_number = generate_random_number()
        print(f"Random integer is: {random_number}")
        random_number_metric.set(random_number)
        time.sleep(15)
