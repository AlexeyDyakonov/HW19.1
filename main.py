from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    file_name = "web.html"

    def get_contex_data(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            contex = file.read()
        return contex

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  #
        self.send_header("Content-type", "text/html")
        self.wfile.write(bytes(self.get_contex_data(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
