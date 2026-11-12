const http = require("node:http");
const { readFile } = require("node:fs");
const { join } = require("node:path");

const pagePath = join(__dirname, "web_speech.html");
const server = http.createServer((request, response) => {
  const pathname = new URL(request.url, "http://localhost").pathname;
  if (pathname !== "/" && pathname !== "/web_speech.html") {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Not found");
    return;
  }

  readFile(pagePath, (error, content) => {
    if (error) {
      console.error("Could not read web_speech.html:", error);
      response.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
      response.end("Could not load the text-to-speech app.");
      return;
    }

    response.writeHead(200, {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
    });
    response.end(content);
  });
});

server.on("error", (error) => {
  console.error("Could not start the local web server:", error.message);
  process.exitCode = 1;
});

server.listen(8000, "127.0.0.1", () => {
  console.log("SpeakEasy is running at http://localhost:8000");
  console.log("Press Ctrl+C to stop the server.");
});
