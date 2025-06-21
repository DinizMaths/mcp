from fastmcp import FastMCP

mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    """

    return f"Current weather in {location}: Sunny, 75°F"

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """
    Resource to get weather information for a specific location.
    """
    return f"Weather resource for {location} is available."

@mcp.prompt()
def weather_report(location: str) -> str:
    """
    Generate a weather report for a specific location.
    """
    return f"The weather in {location} is sunny with a high of 75°F."

if __name__ == "__main__":
    mcp.run(transport="sse", port=8000)