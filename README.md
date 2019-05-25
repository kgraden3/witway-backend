# witway-backend

Steps to Running Backend 
To run backend locally, you must follow the following steps:

1. install docker from https://www.docker.com/products/docker-desktop. Make sure you can use the `docker` command on the command line
2. navigate to the root directory as shown in the dir tree below. 

```.
.
└── witway-backend <-- Root Directory
    ├── Dockerfile
    ├── requirements.txt
    ├── start.sh
    ├── venv
    │   ├── bin
    │   ├── include
    │   ├── lib
    │   └── pyvenv.cfg
    └── witway_backend
        ├── backend
        ├── db.sqlite3
        ├── manage.py
        └── witway_backend
  ```
  3. run `docker build -t witway_backend .` to build the image defined in the dockerfile. 
  This will load the backend into a docker container so you can treat it as a pure input/output.
  It will also install the various packages the backend depends on. Once it completes successfully,
  you should see something like:
  ```
Successfully built f3b67e287c09
Successfully tagged witway_backend:latest
```

4. run `docker run -it -p 8000:8000 witway_backend:latest`. You should see output like this 
```
(venv) ➜  witway-backend git:(master) docker run -it -p 8000:8000 witway_backend:latest
Starting Gunicorn.
[2019-05-25 00:06:55 +0000] [1] [INFO] Starting gunicorn 19.9.0
[2019-05-25 00:06:55 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2019-05-25 00:06:55 +0000] [1] [INFO] Using worker: sync
[2019-05-25 00:06:55 +0000] [10] [INFO] Booting worker with pid: 10
[2019-05-25 00:06:55 +0000] [11] [INFO] Booting worker with pid: 11
[2019-05-25 00:06:55 +0000] [12] [INFO] Booting worker with pid: 12
```
This means the server is running successfully on your local machine's localhost on port 8000. You can reach this by hitting 
http://127.0.0.1:8000 or http//:localhost:8000.

5. Now the fun part. Hitting the above address with no path will result in 
```HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "users": "http://127.0.0.1:8000/users/",
    "user_details": "http://127.0.0.1:8000/user_details/",
    "stakes": "http://127.0.0.1:8000/stakes/",
    "accounts": "http://127.0.0.1:8000/accounts/"
}
```
where each url is the list view/root of an endpoint. Full CRUD can be done on any of them. Loading each of those endpoints 
on your browser will take you to a list view of the given model. Hitting the `Options` button in the upper right hand corner will give you the full range of interaction options for that endpoint. Each model has a url field with a link to its detail view. The url is composed of <server_url>/<model_id>.
Following that link in your browser will lead you to a detail endpoint for that specific model with the same option button, and a delete button for good measure. 

The rule of thumb is:

-list views will return a list with a GET, and will create with a POST

-detail views will return an instance with a GET, and will modify with either a PUT or PATCH.

-All fields are required except for `url` and `id` which will be generated on the backend. 




