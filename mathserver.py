from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="math", version="1.0.0")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise a number to a power"""
    return a ** b  


## Use standard i/p and o/p (stdin and stdout) to communicate with the server (rool funciton call)  This will run in cmd. So working locally.
if __name__ == "__main__":
    mcp.run(transport="stdio")

