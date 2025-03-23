from flask import Flask
import threading
import math

app = Flask(__name__)

def stress_cpu():
    """A function that runs an infinite loop of calculations to increase CPU usage."""
    while True:
        _ = math.sqrt(123456789) * math.sqrt(987654321)

@app.route('/')
def home():
    return "Flask CPU Stress Test Running. Access /stress to increase CPU usage."

@app.route('/stress')
def stress():
    """Starts multiple threads to simulate CPU load."""
    num_threads = 4  # Adjust based on your CPU cores
    for _ in range(num_threads):
        thread = threading.Thread(target=stress_cpu)
        thread.daemon = True  # Ensures threads exit when the program stops
        thread.start()
    return "CPU stress started!"

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


