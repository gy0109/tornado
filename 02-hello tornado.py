import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options
# options模块define语句中同名的配置出现  define会成为全局options属性   入过用户运行了--help会显示define中的default设置
# Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。我们在这里使用这个模块指定我们的应用监听HTTP请求的端口。它的工作流程如下：如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局options的一个属性。如果用户运行程序时使用了--help选项，程序将打印出所有你定义的选项以及你在define函数的help参数中指定的文本。如果用户没有为这个选项指定值，则使用default的值进行代替。Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常。因此，我们允许一个整数的port参数作为options.port来访问程序。如果用户没有指定值，则默认为8000
define('port', default=8888, help='run on the given port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    # 处理请求函数类 根据定义的HTTP方法进行HTTP请求
    def get(self):
        # 查询字符串中取得参数greeting的值（第一个没有就用第二个）
        greeting = self.get_argument('greeting', 'hello')
        # 以一个字符串作为参数 将其写入HTTP响应中
        self.write(greeting+', friendly user!')


if __name__ == '__main__':
    tornado.options.parse_command_line()   # options从命令行读取设置，监听HTTP请求的端口
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])  # 实例化 headlers参数是元组形式的url（正则匹配+对应类函数）
    # 下面代码将会被反复使用，Application对象被创建，将其传入给HTTPserver对象中 在命令行指定端口进行监听  ，，在程序准备好接收HTTP请求后，我们创建一个Tornado的IOLoop的实例。
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




