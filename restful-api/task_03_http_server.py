#!/usr/bin/env python3
"""
Task 03 - Simple API using http.server.

Endpoints:
  /                -> 200 text/plain: greeting
  /data            -> 200 application/json: sample user dict
  /status          -> 200 text/plain: "OK"
  else             -> 404 application/json: {"error": "Endpoint not found"}
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, obj: dict, status: int = 200) -> None:
        payload = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8",
        )
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_text(self, text: str, status: int = 200) -> None:
        data = text.encode("utf-8")
        self.send_response(status)
        self.send_header(
            "Content-Type",
            "text/plain; charset=utf-8",
        )
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/":
            self._send_text("Hello, this is a simple API!", 200)
        elif self.path == "/data":
            self._send_json(
                {"name": "John", "age": 30, "city": "New York"},
                200,
            )
        elif self.path == "/status":
            self._send_text("OK", 200)
        else:
            self._send_json({"error": "Endpoint not found"}, 404)


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Serving on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
