import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define, options
define('port', default=8888, help='run in thr geven', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting+', frendly user!')

    def write_error(self, status_code: int, **kwargs):
        self.write('Gosh darnit user! You caused a %d error.' % status_code)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


