from views import index

def setup_route(app):
    app.router.add_get('/', index)