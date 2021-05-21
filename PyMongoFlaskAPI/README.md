### API for TO-DO App Database

* Install flask using `pip install flask`. <br>
* Install flask-CORS using `pip install -U flask-cors`. <br>
* Using the `port=5555` for API server.<br>
* Run the app using `python3 app.py`.<br>

### Endpoints
* Adding a task <br>
    `http://localhost:5555/add_task` with `POST` request and having a json body like:<br>
    ```
    {
        "task": "Need to complete Geo Homework",
        "done": false
    }
    ```
* Show all the tasks <br>
  `http://localhost:5555/tasks` with `GET` request. <br>
* Show the task <br>
  `http://localhost:5555/show_task/id` with `GET` request.<br>
* Delete one task <br>
* Delete all the tasks <br>
  `http://localhost:5555/delete_all` with `DELETE` request.<br>
* Update the task <br>
  `http://localhost:5000/update_task/id` with `PUT` request and header as: <br>
    ```
    {
        "task": "Need to complete Geo Homework",
        "done": false
    }
    ```