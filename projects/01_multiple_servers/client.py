from fastmcp import Client

config = {
    "mcpServers": {
        "weather": {
            "url": "http://localhost:8000/sse",
        },
        "stock": {
            "url": "http://localhost:8001/sse",
        },
    }
}

async def main():
    async with Client(config) as client:
        tools = await client.list_tools()

        print(f"Tools: {tools}")

        resources = await client.list_resources()

        print(f"Resources: {resources}")

        prompts = await client.list_prompts()

        print(f"Prompts: {prompts}")

        response = await client.call_tool("weather_get_weather", {"location": "New York"})

        print(f"Response: {response}")

        response = await client.call_tool("stock_get_stock", {"symbol": "AAPL"})

        print(f"Response: {response}")

        response = await client.call_tool("stock_get_stock", {"symbol": "WrongSymbol"})

        print(f"Response: {response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())