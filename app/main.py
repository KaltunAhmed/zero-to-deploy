from http.server import BaseHTTPRequestHandler, HTTPServer

# TODO: put your own name here — this will show up in the browser response
NAME = "YOUR NAME HERE"

PORT = 8000


def add(a, b):
    """
    A simple function that adds two numbers together.
    """
    return a + b


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        result = add(2, 3)

        message = (
            f"Hello from {NAME}'s server!\n"
            f"Here's proof the add() function works: add(2, 3) = {result}\n"
        )
        self.wfile.write(message.encode("utf-8"))

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()