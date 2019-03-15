import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
import textwrap

from tornado.options import define, options
define('port', default=8800, help='run in the given port', type=int)  # 设置默认  --help是可以看到 全局属性


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])    # 字符串反转


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')   # 根据字符串传入参数  若第一位参数不存在  则第二位参数为默认
        width = self.get_argument('width', '40')
        # 将字符串作为函数参数传入到HTTP请求中
        # textwrap.fill：文本 指定宽度修饰文本  默认70
        self.write(textwrap.fill(text, int(width)))


if __name__ == '__main__':
    # 解析命令行
    tornado.options.parse_command_line()
    # 创建实例
    app = tornado.web.Application(
        handlers=[
            (r'/reverse/(\w+)', ReverseHandler),
            (r'/wrap', WrapHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
