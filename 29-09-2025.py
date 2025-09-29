from mcp.server import Server
from mcp.server.tools import tool

server = Server("file-server")

@tool
def read_file(path: str) -> str:
    """Read a text file and return its contents."""
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    server.run()
