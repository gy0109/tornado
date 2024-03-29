import os.path
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define, options
define('port', default=8888, help='run on the given post', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')   # render进行页面渲染


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)  # 模板填充 参数一一对应关系


class BookHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('book.html',
                    title='Home page',
                    headers='Books that are great',
                    books=[
                        'Learning Python',
                        'Programing Collective Intelligence',
                        'Restful web services'
                    ])


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
            (r'/poem', PoemPageHandler),
            (r'/book', BookHandler),

        ],
        template_path=os.path.join(os.path.dirname(__file__), 'template')
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()