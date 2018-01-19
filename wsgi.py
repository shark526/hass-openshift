from flask import Flask,request

import subprocess
application = Flask(__name__)

if __name__ == "__main__":
    application.run()
    bashCmd = "hass --open-ui"
    subprocess.Popen(bashCmd)

