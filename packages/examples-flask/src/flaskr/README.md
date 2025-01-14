# Tutorial - flaskr

## References

- [Tutorial - Flask Documentation](https://flask.palletsprojects.com/en/stable/tutorial/)

## Getting started

Install dependencies:

```shell
uv sync
```

Create a database:

```shell
flask --app flaskr init-db
```

Run the server:

```shell
flask --app flaskr run 
```

or using uwsgi:

```shell
uvx uwsgi --ini uwsgi.ini:flaskr --venv $VIRTUAL_ENV
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>
