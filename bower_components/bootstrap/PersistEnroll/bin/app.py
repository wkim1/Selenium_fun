import web

urls = (
  '/', 'Index',
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(className="CS193P")
        greeting = " %s" % (form.className)
        return render.index(greeting = greeting)

class inputClass(object):
    def POST(self):
        form = web.input(className="CS193P")
        greeting = " %s" % (form.className)
        return render.index(greeting = greeting)


if __name__ == "__main__":
    app.run()