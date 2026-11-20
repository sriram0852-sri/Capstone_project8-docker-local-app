from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>Docker Project 8</title>
        </head>
        <body>
            <h1>Docker App Running Successfully!</h1>
            <h2>Project 8: Build and Run Docker App Locally</h2>
            <p>Container deployment is successful.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Docker application running on port 5000")

server.serve_forever()
