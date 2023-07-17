# react flask minimum
Minimum code to start a react flask project

## Run Client in Development Mode
    cd client
    npm start

## Run Server in Development Mode
    cd server
    flask run

## Run Client, Server and Reverse Proxy in Production Mode

### Docker

Build Services and run Contaiers

    docker-compose up -d 

Rebuild Service(s)

    docker-compose up --build --force-recreate --no-deps [-d] [<service_name>..]

Options:
| Flag  |  Description |
|---|---|
| `-d, --detach`  | Detached mode: Run containers in the background, print new container names. Incompatible with `--abort-on-container-exit`. |
| `--no-deps`  | Don't start linked services. |
| `--force-recreate`  | Recreate containers even if their configuration and image haven't changed. |

| `--build`  | Build images before starting containers. |


# Pycharm Proffesional 
1. Pycharm -> Preferences -> Build, Execution, Deployment -> Docker
* Press + (Add)
* Connect to Docker daemon with: Docker for Mac
* Navigate to Docker -> Tools
* Docker Machine executable: `/usr/local/bin/docker-machine`
* Docker Compose executable: `/usr/local/bin/docker-compose`
2. Navigate to Preferences -> Project -> Project Interpreter
3. Locate “gear” icon -> Add remote -> Docker Compose
1. Server: Choose your previously created Docker server
2. Configuration file: Locate your project’s `docker-compose.yml` file
3. Service: Set your main service here
4. If not set, select newly created Remote Python interpreter in “Project Interpreter” field.
5. Run -> Edit Configurations - Add -> Python
6. Setup appropriate fields as follows
* Script path: `/usr/local/bin/gunicorn`
* Parameters: `app:application -b 0.0.0.0:80 -t 0`
7. Press OK button
8. Now you should be able to use PyCharm debugger



#Code 
flask:
	docker-compose run --rm -e FLASK_APP=server.py -e FLASK_ENV=development --service-ports backend  
flaskdebug:
	docker-compose run --rm -e DEBUGGER=True -e FLASK_APP=app.py -e FLASK_ENV=development --service-ports flask-server flask run --host 0.0.0.0



## gunicorn  
gunicorn:
	docker-compose run --rm --service-ports flask-server gunicorn --reload --bind 0.0.0.0:5000 app:app
gunicorndebug:
	docker-compose run --rm -e DEBUGGER=True --service-ports flask-server gunicorn --reload --bind 0.0.0.0:5000 --timeout 3600 app:app

https://blog.theodo.com/2020/05/debug-flask-vscode/ 7

>> DEBUG=True now is defined on .env

