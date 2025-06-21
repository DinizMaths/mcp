from fastmcp import FastMCP

mcp = FastMCP("Stock Service")

@mcp.tool()
def get_stock(symbol: str) -> str:
    """
    Get the current stock price for a given symbol.
    """

    if symbol.upper() == "AAPL":
        return "Current stock price for AAPL: $150.00"
    elif symbol.upper() == "GOOGL":
        return "Current stock price for GOOGL: $2800.00"
    else:
        return f"Stock price for {symbol} is not available."

@mcp.resource("stock://{symbol}")
def stock_resource(symbol: str) -> str:
    """
    Resource to get stock information for a specific symbol.
    """

    if symbol.upper() == "AAPL":
        return "Stock resource for AAPL is available."
    elif symbol.upper() == "GOOGL":
        return "Stock resource for GOOGL is available."
    else:
        return f"Stock resource for {symbol} is not available."

if __name__ == "__main__":
    mcp.run(transport="sse", port=8001)