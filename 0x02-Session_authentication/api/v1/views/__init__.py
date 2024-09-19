# api/v1/views/__init__.py
#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from . import index
from . import users
from . import session_auth
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views here to avoid circular import issues

User.load_from_file()
