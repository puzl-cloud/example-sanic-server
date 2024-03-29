# What is it

Simple HTTP/HTTPS server to use in a Docker container with Python pre-installed for test proposals (example for [Puzl cloud](https://puzl.cloud)). Server runs Swagger API on `1616` port.

# Requirements

- Python 3.6 or higher
- `requirements.txt`

All the requirements are installing in `run.sh` file, which should be set as a Docker entry point.

# Using in puzl.cloud dashboard
## Run 
### Docker image

Choose any Docker image, contains the needed version of Python.

### Git repository
To use your repo from Github without ssh inside a Docker container, [generate](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and use personal access token.

For Github:
```
https://a72db2630fa574a11445c16e6824617e4c3d8017@github.com/puzl-ee/example-sanic-server.git
```
To clone repo from Gitlab, use this format:
```
https://{USER}:{TOKEN}@gitlab.com/repository_path.git
```

### Entry point
This will install all `requirements.txt` and run application then.
```bash
bash ./run.sh
```

### Swagger port

Add port `1616` via Puzl dashboard. 

![Open port in Puzl dashboard](port-screenshot.png?raw=true "Open port")

Kubernetes `Service` will be created for your pod automatically.

### Environment variables

You can define your own port, if needed.

`LISTEN_PORT` - Swagger API, default `1616`

## Use

After your pod is up and running in Puzl's Kubernetes cluster, you can access it by a given external port and host name.

`http://host:external_port/swagger`

### Routes

`/health` - used to check health

`/swagger` - Swagger endpoint
