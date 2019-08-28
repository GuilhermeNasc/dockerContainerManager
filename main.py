import docker
from flask import Flask, render_template

app = Flask(__name__)

client = docker.from_env()

@app.route('/')
def hello_world():
    containers = client.containers.list(all=True)
    print(containers)
    return render_template('index.html', containers=containers)


if __name__ == "__main__":
    aux = client.containers.list(all=True)[0]
    print(aux.name)
    app.run(debug=True)