import web
from handle import Handle

render = web.template.render('views/')

urls = (
    '/', 'index',
    '/wx','Handle',
)

class index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()