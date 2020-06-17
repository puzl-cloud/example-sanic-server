from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

from models import Health


health_blueprint = Blueprint('health', '/health')


@health_blueprint.get("/", strict_slashes=False)
@doc.summary("Does the service feel ok?")
@doc.produces(Health)
async def check_health(request):
    return json({"status": True})
