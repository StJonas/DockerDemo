from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host="redis", port=6379)

# Define the file path
file_path = "/data/message.txt"


@app.route("/")
def hello():
    # Set a value in Redis
    r.set("message", "Welcome to the Docker Tutorial!")

    # Retrieve the value from Redis
    message = r.get("message").decode("utf-8")

    # Write the message to a file
    with open(file_path, "w") as file:
        file.write(message)

    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
