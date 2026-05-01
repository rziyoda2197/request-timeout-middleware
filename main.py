import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def timeout_decorator(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time - start_time > timeout:
                return jsonify({"error": "Timeout error"}), 408
            return result
        return wrapper
    return decorator

@app.route('/example', methods=['GET'])
@timeout_decorator(5)  # 5 second timeout
def example():
    time.sleep(6)  # Simulate a long-running operation
    return jsonify({"message": "Hello, World!"})

@app.errorhandler(408)
def request_timeout_handler(e):
    return jsonify({"error": "Request timeout"}), 408

if __name__ == '__main__':
    app.run(debug=True)
```

```python
import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def timeout_decorator(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time - start_time > timeout:
                return jsonify({"error": "Timeout error"}), 408
            return result
        return wrapper
    return decorator

@app.route('/example', methods=['GET'])
@timeout_decorator(5)  # 5 second timeout
def example():
    time.sleep(6)  # Simulate a long-running operation
    return jsonify({"message": "Hello, World!"})

@app.errorhandler(408)
def request_timeout_handler(e):
    return jsonify({"error": "Request timeout"}), 408

if __name__ == '__main__':
    app.run(debug=True)
