import web
from handle import Handle

render = web.template.render('views/')

urls = (
    '/', 'index',
    '/wx','Handle',
    '/bus', 'bus',
)

class index:
    def GET(self):
        return render.index()

class bus:
    def GET(self):
        return render.bus()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()