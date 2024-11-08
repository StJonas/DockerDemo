from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host="redis", port=6379)

# Define the file path
file_path = "/data/message.txt"


@app.route("/")
def hello():
    # Increment the counter
    count = r.incr("hello_count")

    # Set a value in Redis
    r.set("message", "Welcome to the Docker Tutorial!")

    # Retrieve the value from Redis
    message = r.get("message").decode("utf-8")

    # Write the message and count to a file
    with open(file_path, "w") as file:
        file.write(f"{message}\nHello has been called {count} times.")

    return f"{message}\nHello has been called {count} times."


@app.route("/read-file")
def read_file():
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
            return jsonify({"file_content": content})
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
