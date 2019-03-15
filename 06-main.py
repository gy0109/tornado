import os.path
import random
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options
define('port', default=8898, help='run in 8888', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index1.html')


class MungedPageHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                    mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        print(source_map)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines, choice=random.choice)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/poem', MungedPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'template'),   # 模板文件
        static_path=os.path.join(os.path.dirname(__file__), 'static'),  # 静态文件
        debug=True    # debug模式
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()



