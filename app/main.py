from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Yash Babu"  # Replace with your full name
    try:
        username = os.getlogin()
    except:
        username = os.environ.get("USER", "unknown")

    tz = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.getoutput("top -b -n1 | head -n 20")

    return f"""
    <pre>
Name: {name}
Username: {username}
Server Time (IST): {ist_time}

TOP output:
{top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
