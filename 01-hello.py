import tornado.ioloop
import tornado.web
import os
# RequestHandler Applications处理请求


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write('hello world')
        self.render('base.html')


class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('500.html')


def make_app():
    return tornado.web.Application(
        [
            (r'/', MainHandler),
            (r'/500', ErrorHandler),
        ],
        template_path=os.path.join(
            os.path.dirname(__file__), 'template'
    ),
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

