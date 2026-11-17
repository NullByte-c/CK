import time
import requests

try:
    from config import WEBHOOK_URL
except ImportError:
    WEBHOOK_URL = ""

running = True
iterations = 0

def send_status(status):
    if not WEBHOOK_URL:
        print("Webhook URL is not configured.")
        return

    try:
        response = requests.post(
            WEBHOOK_URL,
            json={"content": status},
            timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        print("Webhook error:", exc)

def initialize():
    global running, iterations
    running = True
    iterations = 0
    send_status("ONLINE - Cookie Clicker opened")

def background_task():
    if iterations > 0 and iterations % 10 == 0:
        send_status("ONLINE - Cookie Clicker running")

def run_once():
    global iterations

    if not running:
        return

    iterations += 1
    background_task()

def shutdown():
    global running

    if running:
        running = False
        send_status("OFFLINE - Cookie Clicker closed")
