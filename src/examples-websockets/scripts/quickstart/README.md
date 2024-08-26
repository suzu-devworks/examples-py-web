# Quick start

## Table of Contents <!-- omit in toc -->

- [Quick start](#quick-start)
  - [Say “Hello world!”](#say-hello-world)
  - [Encrypt connections](#encrypt-connections)
  - [Connect from a browser](#connect-from-a-browser)
  - [Broadcast messages](#broadcast-messages)
  - [Manage application state](#manage-application-state)
  - [More documents](#more-documents)


## Say “Hello world!”

Start the server:

```shell
python scripts/quickstart/server.py
```

The client connects to the server and receives the response:

```shell
python scripts/quickstart/client.py
```


## Encrypt connections

The connection is encrypted with TLS (Transport Layer Security),
wss requires certificates like https.

We'll use the development SSL certificate here

Start the server:

```shell
python scripts/quickstart/server_secure.py
```

The client connects to the server and receives the response:

```shell
python scripts/quickstart/client_secure.py
```


## Connect from a browser

Start the server:

```shell
python scripts/quickstart/show_time.py
```

Start the http server:

```shell
python -m http.server 8000

# or

pdm run dev
```

Access to url:

- <http://localhost:8000/scripts/quickstart/show_time.html>


## Broadcast messages

Start the server:

```shell
python scripts/quickstart/show_time_2.py
```

Start the http server:

```shell
pdm run dev
```

Accessing a URL using multiple browsers:

- <http://localhost:8000/scripts/quickstart/show_time.html>


## Manage application state

Start the server:

```shell
python scripts/quickstart/counter.py
```

Start the http server:

```shell
pdm run dev
```

Accessing a URL using multiple browsers:

- <http://localhost:8000/scripts/quickstart/counter.html>


## More documents

- <https://websockets.readthedocs.io/en/stable/howto/quickstart.html>
