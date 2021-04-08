from flask_restx import Resource, Api, Namespace

User = Namespace(
    name="User",
    description="APIs for user"
)
