# -*- coding: utf-8 -*-

"""
123
"""

from aiohttp import web
from routes import setup_route
from init_db import init_db, close_db
from config import config


app = web.Application()
app['config'] = config
app.on_startup.append(init_db)
app.on_cleanup.append(close_db)
setup_route(app)
web.run_app(app)