import web
from handle import Handle

urls = (
    '/', 'index',
    '/wx','Handle',
)

class index:
    def GET(self):
        render = web.template.render('views/index')
        return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()