import json
import os


def load_env_to_sanic_app(app, env_name, default=None, env_type=str, required=True):
    class Env:
        pass

    env_val = os.getenv(env_name, default)
    if env_val is None and required:
        raise Exception(f"{env_name} is required")

    if env_type is not str:
        if env_type is list or env_type is dict:
            env_val = json.loads(env_val)
        else:
            env_val = env_type(env_val)
    try:
        app.env
    except Exception as e:
        app.env = Env()
    setattr(app.env, env_name.lower(), env_val)
