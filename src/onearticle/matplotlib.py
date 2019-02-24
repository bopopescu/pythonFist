import web

urls = (
    '/index', 'index',
    '/hello', 'hello',
    '/page/\d+', 'page',
    '/first', 'first',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'

)
app = web.application(urls, globals())


class blog:
    def POST(self):
        query = web.input()
        return query


class page:
    def GET(self):
        data = web.input()
        return data


class first:
    def GET(self):
        return open(r'data.html', 'r').read()


class index:
    def GET(self, name):
        if not name:
            name = 'World'
        return open(r'index.html', 'r').read()


class hello:
    def GET(self, name):
        return "wang"


if __name__ == "__main__":
    app.run()
